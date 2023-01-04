#!/usr/bin/env python3
from ev3dev2.button import Button
from time import sleep
import requests
import uuid

btn = Button()
sid = uuid.uuid4()

requests.post('https://panel-party-ws.fly.dev/join', json={'sid': str(sid)})


def left(state):
    print('Left button pressed' if state else 'Left button released')
    requests.post('https://panel-party-ws.fly.dev/key', json={'key': 'LEFT', 'sid': str(sid)})
    # socket.emit('keyPress', {"key": "LEFT", "sid": socket.get_sid()})


def right(state):  # neater use of 'if' follows:
    print('Right button pressed' if state else 'Right button released')
    requests.post('https://panel-party-ws.fly.dev/key', json={'key': 'RIGHT', 'sid': str(sid)})
    # socket.emit('keyPress', {"key": "RIGHT", "sid": socket.get_sid()})


def up(state):
    print('Up button pressed' if state else 'Up button released')
    requests.post('https://panel-party-ws.fly.dev/key', json={'key': 'UP', 'sid': str(sid)})
    # socket.emit('keyPress', {"key": "UP", "sid": socket.get_sid()})


def down(state):
    print('Down button pressed' if state else 'Down button released')
    requests.post('https://panel-party-ws.fly.dev/key', json={'key': 'DOWN', 'sid': str(sid)})
    # socket.emit('keyPress', {"key": "DOWN", "sid": socket.get_sid()})


def enter(state):
    print('Enter button pressed' if state else 'Enter button released')
    # socket.emit('keyPress', {"key": "ENTER", "sid": socket.get_sid()})


btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter

# This loop checks button states continuously (every 0.01s). 
# If the new state differs from the old state then the appropriate
# button event handlers are called.
while True:
    btn.process()
    sleep(0.01)