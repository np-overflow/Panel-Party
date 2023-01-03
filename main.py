#!/usr/bin/env python3
from ev3dev2.button import Button
from time import sleep


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.


# Write your program here.


btn = Button()

# Do something when state of any button changes:
  
def left(state):
    if state:
        print('Left button pressed')
    else:
        print('Left button released')
    
def right(state):  # neater use of 'if' follows:
    print('Right button pressed' if state else 'Right button released')
    
def up(state):
    print('Up button pressed' if state else 'Up button released')
    
def down(state):
    print('Down button pressed' if state else 'Down button released')
    
def enter(state):
    print('Enter button pressed' if state else 'Enter button released')
    
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