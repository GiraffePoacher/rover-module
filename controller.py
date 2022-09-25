import socket
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
        return 255
    elif x < 0:
        return 0    
    else:
        return x

pg.init()
pg.joystick.init()
j = pg.joystick.Joystick(0)
j.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
#think about appropriate data set for the wheel stuff

leftWheel1 = leftWheel2 = leftWheel3 = rightWheel1 = rightWheel2 = rightWheel3 = 128

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

                movepacket = ("DriveCommand_"+str(check(leftWheel1))+"_"+str(check(rightWheel1))+"_"+str(check(leftWheel2))+"_"+str(check(rightWheel2))+"_"+str(check(leftWheel3))+"_"+str(check(rightWheel3)))
                print(movepacket)
                send(movepacket)

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





