import socket
import pygame as pg

loop = True

pg.init()
pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]

#print(pg.joystick.Joystick.get_id())

while loop:
    for event in pg.event.get():
        if event.type == pg.JOYBUTTONDOWN:
            print(event)
            exit(0)
        elif event.type == pg.JOYHATMOTION:
            print(event)




