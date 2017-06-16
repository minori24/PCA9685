# Servo Controller

import pca9685
import smbus

class ServoController:

    SERVO_MAX = 2000
    SERVO_MIN = 1000
    SERVO_CENTER = 1500
    mag_x = 100
    mag_y = 100
    servo_x = SERVO_CENTER
    servo_y = SERVO_CENTER

    def __init__(self):
        bus = smbus.SMBus(1)
        driver = pca9685.PCA9685(I2CBus=1, I2CAddr=0x40, freq=50)

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

        driver.setPulseWidth(0, x)
        driver.setPulseWidth(1, y)

    def moveMouth(self, openclose):

if __name__ == '__main__':
    
