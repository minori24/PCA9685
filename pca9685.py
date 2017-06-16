# PCA9685 PWM Driver Library

import smbus

class PCA9685:

    addr = 0x40
    freq = 20000

    def __init__(self, I2CBus, I2CAddr, freq):
        self.bus = smbus.SMBus(I2CBus)
        self.addDevice(I2CAddr)
        self.setPWMFreq(freq)

    def addDevice(self, I2CAddr):
        self.addr = I2CAddr
        self.bus.write_byte_data(self.addr, 0x00, 0x01)
        self.bus.write_byte_data(self.addr, 0x01, 0x04)

    def setPWMFreq(self, PWMfreq):
        # set prescaler
        # clock source: internal 25MHz
        self.freq = PWMfreq
        prs = 25000000 / (4096 * self.freq) - 1

        # write prescaler value / restart PWM output
        self.bus.write_byte_data(self.addr, 0x00, 0x10)
        self.bus.write_byte_data(self.addr, 0xFE, int(prs))
        self.bus.write_byte_data(self.addr, 0x00, 0x01)

    def setPulseWidth(self, ch, microseconds):
        if(ch < 15 and ch > 0):
            reg_on_h = 7 + 4 * ch
            reg_on_l = 6 + 4 * ch
            reg_off_h = 9 + 4 * ch
            reg_off_l = 8 + 4 * ch

            on = 4096 - microseconds / self.freq * 4096
            off = 0

            self.bus.write_byte_data(addr, reg_on_l, int(on) & 0xFF)
            self.bus.write_byte_data(addr, reg_on_h, (int(on) & 0x0F00) >> 8)
            self.bus.write_byte_data(addr, reg_off_l, int(off) & 0xFF)
            self.bus.write_byte_data(addr, reg_off_h, (int(off) & 0x0F00) >> 8)
