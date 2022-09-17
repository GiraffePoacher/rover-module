import socket
import pygame as pg

host = socket.gethostname()
port = 5555

loop = True


pg.init()
pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]

#print(pg.joystick.Joystick.get_id())

while loop:
    for event in pg.event.get():
        if event.type == pg.JOYBUTTONDOWN:
            print(event)
            
            exit(0) #for testing
        elif event.type == pg.JOYHATMOTION:
            print(event)
        elif event.type == pg.JOYDEVICEREMOVED:
            print('EXITTING DEVICE REMOVED')
            exit(0)




