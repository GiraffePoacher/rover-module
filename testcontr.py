from http import client
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
                print("o is pressed, instastop") #resets the values to stop rover
                leftWheel1 = 128
                leftWheel2 = 128
                leftWheel3 = 128
                rightWheel1 = 128
                rightWheel2 = 128
                rightWheel3 = 128
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
                leftWheel1 += 10
                leftWheel2 += 10
                leftWheel3 += 10
                rightWheel1 -= 10
                rightWheel2 -= 10
                rightWheel3 -= 10

                check(leftWheel1)
                check(leftWheel2)
                check(leftWheel3)
                check(rightWheel1)
                check(rightWheel2)
                check(rightWheel3)

                print("right")   
            if input == (0,1):
                leftWheel1 += 10
                leftWheel2 += 10
                leftWheel3 += 10
                rightWheel1 += 10
                rightWheel2 += 10
                rightWheel3 += 10

                check(leftWheel1)
                check(leftWheel2)
                check(leftWheel3)
                check(rightWheel1)
                check(rightWheel2)
                check(rightWheel3)

                print("up")
            if input == (-1,0):
                leftWheel1 -= 10
                leftWheel2 -= 10
                leftWheel3 -= 10
                rightWheel1 += 10
                rightWheel2 += 10
                rightWheel3 += 10

                check(leftWheel1)
                check(leftWheel2)
                check(leftWheel3)
                check(rightWheel1)
                check(rightWheel2)
                check(rightWheel3)

                print("left")    
            if input == (0,-1):
                leftWheel1 -= 10  #change the values 
                leftWheel2 -= 10
                leftWheel3 -= 10
                rightWheel1 -= 10
                rightWheel2 -= 10
                rightWheel3 -= 10

                check(leftWheel1)  #check if values are within given range
                check(leftWheel2)
                check(leftWheel3)
                check(rightWheel1)
                check(rightWheel2)
                check(rightWheel3)

                                    #send packet

                print("down")     

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