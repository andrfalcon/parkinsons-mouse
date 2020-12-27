from pynput.mouse import Button, Controller

appIsOpen = True
mouse = Controller()

# Read the pointer position
while appIsOpen:
    print('The current pointer position is {0}'.format(mouse.position))