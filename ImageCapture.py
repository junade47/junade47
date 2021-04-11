from djitellopy import tello
import cv2

terra = tello.Tello()
terra.connect()
print(terra.get_battery())

terra.streamon()

while True:
    img = terra.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)