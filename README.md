# rover-module
R3 mod1 exersize 

while True:
    for event in pg.event.get():
        if event.type == pg.JOYBUTTONDOWN:
            print(event)
            
            exit(0) #for testing
        elif event.type == pg.JOYHATMOTION:
            print(event)
        elif event.type == pg.JOYDEVICEREMOVED:
            print('EXITTING DEVICE REMOVED')
            exit(0)