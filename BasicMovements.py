from djitellopy import tello
from time import sleep

terra = tello.Tello()
terra.connect()
print(terra.get_battery())

terra.takeoff()
terra.send_rc_control(0, 50, 0, 0)
sleep(2)
terra.send_rc_control(0, 0, 0, 100)
sleep(2)
terra.send_rc_control(0, 0, 50, 0)
sleep(2)
terra.send_rc_control(0, 50, 0, 0)
sleep(2)
terra.send_rc_control(0, 0, 0, 100)
sleep(2)
terra.send_rc_control(0, 0, 0, 0)
terra.land()
