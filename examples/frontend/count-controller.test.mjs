import test from 'node:test';
import assert from 'node:assert/strict';
import {createCountController} from './count-controller.mjs';

function setup() {
    const pending = [];
    let view = {kind: 'initial'};
    const controller = createCountController({
        analyze: () => new Promise((resolve, reject) => pending.push({resolve, reject})),
        showPending: () => { view = {kind: 'pending'}; },
        showStats: value => { view = {kind: 'stats', value}; },
        showError: message => { view = {kind: 'error', message}; },
    });
    return {controller, pending, getView: () => view};
}

test('a slower old reply cannot overwrite a newer reply', async () => {
    const {controller, pending, getView} = setup();
    const oldRequest = controller.update('a');
    const newRequest = controller.update('abc');
    const latest = {runes: 3, bytes: 3, lines: 1};
    pending[1].resolve(latest);
    await newRequest;
    pending[0].resolve({runes: 1, bytes: 1, lines: 1});
    await oldRequest;
    assert.deepEqual(getView(), {kind: 'stats', value: latest});
});

test('clear invalidates an outstanding request', async () => {
    const {controller, pending, getView} = setup();
    const request = controller.update('abc');
    controller.clear();
    pending[0].resolve({runes: 3, bytes: 3, lines: 1});
    await request;
    assert.deepEqual(getView(), {kind: 'stats', value: {runes: 0, bytes: 0, lines: 0}});
});

test('a failed latest request shows an error, not stale counts', async () => {
    const {controller, pending, getView} = setup();
    const request = controller.update('abc');
    assert.equal(getView().kind, 'pending');
    pending[0].reject(new Error('bridge failure'));
    await request;
    assert.equal(getView().kind, 'error');
});

test('an old failure cannot replace a newer success', async () => {
    const {controller, pending, getView} = setup();
    const first = controller.update('a');
    const second = controller.update('日本語');
    const latest = {runes: 3, bytes: 9, lines: 1};
    pending[1].resolve(latest);
    await second;
    pending[0].reject(new Error('old request failed'));
    await first;
    assert.deepEqual(getView(), {kind: 'stats', value: latest});
});
