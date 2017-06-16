# Servo Controller

import pca9685
import smbus
import random
import time

class ServoController:

    SERVO_MAX = 2000
    SERVO_MIN = 1000
    SERVO_CENTER = 1500
    mag_x = 100
    mag_y = 100
    servo_x = SERVO_CENTER
    servo_y = SERVO_CENTER

    def __init__(self):
        self.driver = pca9685.PCA9685(I2CBus=1, I2CAddr=0x40, freq=47)

    # deltaX, deltaY: distances(px) from target to camera center
    def moveXY(self, deltaX, deltaY):
        x = self.servo_x + deltaX * mag_x
        y = self.servo_y + deltaY * mag_y

        if (x > self.SERVO_MAX):
            x = self.SERVO_MAX

        if (x < self.SERVO_MIN):
            x = self.SERVO_MIN

        if (y > self.SERVO_MAX):
            y = self.SERVO_MAX

        if (y < self.SERVO_MIN):
            y = self.SERVO_MIN

        self.driver.setPulseWidth(0, x)
        self.driver.setPulseWidth(1, y)

    def moveAbsoluteX(self, position):
        self.driver.setPulseWidth(0, position)

    def moveAbsoluteY(self, position):
        self.driver.setPulseWidth(1, position)

    def moveAbsoluteMouth(self, position):
        self.driver.setPulseWidth(2, position)

    def moveMouth(self, openclose):
        pass

if __name__ == '__main__':
    servo = ServoController()

    while True:
        rx = random.randint(1000, 2000)
        ry = random.randint(1000, 2000)
        rm = random.randint(1000, 2000)
        print("x:" + str(rx) + " y:" + str(ry) + " mouth:" + str(rm))
        servo.moveAbsoluteX(rx)
        servo.moveAbsoluteY(ry)
        servo.moveAbsoluteMouth(rm)
        time.sleep(1.0)
