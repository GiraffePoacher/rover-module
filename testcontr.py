from http import client
from mimetypes import init
import pygame as pg
import numpy as np

pg.init()
pg.joystick.init()
j = pg.joystick.Joystick(0)
j.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
#think about appropriate data set for the wheel stuff

leftWheel1 = leftWheel2 = leftWheel3 = rightWheel1 = rightWheel2 = rightWheel3 = 128

def check(x):
    if x < 255:
        return 255
    elif x < 0:
        return 0    
    else:
        return x

while True:
    for event in pg.event.get():

        if event.type == pg.JOYBUTTONDOWN:
            print(event.dict, event.joy, event.button, 'pressed')
            if j.get_button(0):
                print("x is pressed") 
            if j.get_button(1):
                print("o is pressed") 
            if j.get_button(2):
                print("tri is pressed")
            if j.get_button(3):
                print("squ is pressed") 
            if j.get_button(6): #L2 quits out the program
                exit(0) 
        elif event.type == pg.JOYHATMOTION:
            input = event.value
            print(event.value)
            if input == (1,0):
                print("x = 1, right")   
            if input == (0,1):
                print("y = 1 up")
            if input == (-1,0):
                print("x=-1 left")    
            if input == (0,-1):
                print("x=-1 down")  
            if input == (1,1):
                print("diag 1,1")
            if input == (-1,1):
                print("diag -1,1")
            if input == (1,-1):
                print("diag 1,-1")
            if input == (-1,-1):
                print("diag -1,-1")  

        elif event.type == pg.JOYDEVICEREMOVED:
            print('EXITTING DEVICE REMOVED')
            exit(0)

        #if event.type == pg.JOYBUTTONDOWN:
        #    if event.key == pg.CONTROLLER_BUTTON_A:
        #    print(event.dict, event.joy, event.button, 'pressed')
        #    print(event)



        #    print(event.dict, event.joy, event.button, 'pressed')
        #    print(event)
        #    if event.key == event.button:
        #        print("x is pressed")

#https://www.programcreek.com/python/example/121887/pygame.JOYHATMOTION reserach joyhatmotion and how it works