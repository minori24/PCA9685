import servo
import detect_haar


haar = detect_haar.Detect_HAAR()
servo = servo.ServoConrtoller()

servo.moveXY(0, 0)

while True:
    rect = haar.detect()
    
    if (rect > 0):
        center = [0, 0]
        servo.moveXY(center[0], center[1])