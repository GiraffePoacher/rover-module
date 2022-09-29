import socket
from sys import setswitchinterval
import pygame as pg

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DC_MSG = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

def check(x):
    if x > 255:
        x = 255
        return 255
    elif x < 0:
        x = 0
        return 0    
    else:
        return x

def checkarm(x):   #I could of added other parameters in the def to make one work on all, but setting all the parameters for everytime this 
                    #gets called would be really annoying
    if x > 148:
        x = 148
        return 148
    elif x < 108:
        x = 108
        return 108    
    else:
        return x

def checkhoist(x):
    if x > 148:
        x = 148
        return 148
    elif x < 128:
        x = 128
        return 128    
    else:
        return x

#hoist should not be 128 or else it falls 
#pwm 128 is resting 108 closed and 148 open?
#+/- 30 pwm 

pg.init()
pg.joystick.init()
j = pg.joystick.Joystick(0)
j.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]

leftWheel1 = leftWheel2 = leftWheel3 = rightWheel1 = rightWheel2 = rightWheel3 = 128
hoist = 138
upperExtender = lowerExtender = screwDriver = claw = swivel = 128

while True:
    for event in pg.event.get():
                                    #finish this at school
        if event.type == pg.JOYBUTTONDOWN:
            print(event.dict, event.joy, event.button, 'pressed')
            if j.get_button(0): #screwdriver down
                print("x") 
                screwDriver -= 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(1): #claw up
                print("o")
                claw += 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(2): #screw up
                print("tri")
                screwDriver += 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(3): #claw down
                print("square") 
                claw -= 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(4): #- upperextend
                print("L1")
                upperExtender -= 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(5):
                print("R1") 
                lowerExtender -= 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(6): # + upper extender 
                print("L2") 
                upperExtender += 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket)
            if j.get_button(7): # use analog sticks for the arm extenders 
                print("R2") 
                lowerExtender += 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(11): # use analog sticks for the arm swivel  dec
                print("L analog") 
                swivel -= 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(12): # use analog sticks for the arm swivel inc
                print("R analog") 
                swivel += 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(9):
                print("start is pressed") #hoist up
                hoist += 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
            if j.get_button(8):
                print("select is pressed") #hoist down
                hoist -= 4
                armpacket = ("ArmCommand_"+str(checkarm(upperExtender))+"_"+str(checkarm(lowerExtender))+"_"+str(checkarm(screwDriver))+"_"+str(checkarm(claw))+"_"+str(checkhoist(hoist))+"_"+str(checkarm(swivel)))
                print(armpacket)
                send(armpacket) 
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

                movepacket = ("DriveCommand_"+str(check(leftWheel1))+"_"+str(check(rightWheel1))+"_"+str(check(leftWheel2))+"_"+str(check(rightWheel2))+"_"+str(check(leftWheel3))+"_"+str(check(rightWheel3)))
                print(movepacket)
                send(movepacket)
                print("right")   
            if input == (0,1):
                leftWheel1 += 10
                leftWheel2 += 10
                leftWheel3 += 10
                rightWheel1 += 10
                rightWheel2 += 10
                rightWheel3 += 10

                movepacket = ("DriveCommand_"+str(check(leftWheel1))+"_"+str(check(rightWheel1))+"_"+str(check(leftWheel2))+"_"+str(check(rightWheel2))+"_"+str(check(leftWheel3))+"_"+str(check(rightWheel3)))
                print(movepacket)
                send(movepacket)

                print("up")
            if input == (-1,0):
                leftWheel1 -= 10
                leftWheel2 -= 10
                leftWheel3 -= 10
                rightWheel1 += 10
                rightWheel2 += 10
                rightWheel3 += 10

                movepacket = ("DriveCommand_"+str(check(leftWheel1))+"_"+str(check(rightWheel1))+"_"+str(check(leftWheel2))+"_"+str(check(rightWheel2))+"_"+str(check(leftWheel3))+"_"+str(check(rightWheel3)))
                print(movepacket)
                send(movepacket)

                print("left")    
            if input == (0,-1):
                leftWheel1 -= 10  #change the values 
                leftWheel2 -= 10
                leftWheel3 -= 10
                rightWheel1 -= 10
                rightWheel2 -= 10
                rightWheel3 -= 10

                movepacket = ("DriveCommand_"+str(check(leftWheel1))+"_"+str(check(rightWheel1))+"_"+str(check(leftWheel2))+"_"+str(check(rightWheel2))+"_"+str(check(leftWheel3))+"_"+str(check(rightWheel3)))
                print(movepacket)
                send(movepacket)

                 #send packet

                print("down")     

        elif event.type == pg.JOYDEVICEREMOVED:
            print('EXITTING DEVICE REMOVED')
            exit(0)





