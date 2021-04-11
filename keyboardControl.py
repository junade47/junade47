from djitellopy import tello
import  KeyPressModule as kp
from time import sleep

kp.init()
terra = tello.Tello()
terra.connect()
print(terra.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("RIGHT"):
        lr = speed
    elif kp.getKey("LEFT"):
        lr = -speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = speed
    elif kp.getKey("d"):
        yv = -speed

    if kp.getKey("q"):
        terra.land()

    if kp.getKey("e"):
        terra.takeoff()

    return [lr, fb, ud, yv]

while True:

    vals = getKeyboardInput()
    terra.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)