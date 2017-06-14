# PCA9685 PWM Driver Library

import smbus

class PCA9685:

    addr = 0x40
    bus = None
    freq = 20000
    
    def __init__(self, I2CBus):
        self.bus = I2CBus

    def addDevice(I2CAddr):
        self.addr = I2CAddr
        bus.write_byte_data(addr, 0x00, 0x01)
        bus.write_byte_data(addr, 0x01, 0x04)

    def setPWMFreq(self, PWMfreq):
        # set prescaler
        # clock source: internal 25MHz
        self.freq = PWMfreq
        prs = 25000000 / (4096 * self.freq) - 1

        # write prescaler / restart PWM output
        bus.write_byte_data(addr, 0x00, 0x10)
        bus.write_byte_data(addr, 0xFE, int(prs))
        bus.write_byte_data(addr, 0x00, 0x01)

    def setPulseWidth(self, ch, microseconds):
        on = 4096 - microseconds / self.freq * 4096
        off = 0

        bus.write_byte_data(addr, 0x06, int(on) & 0xFF)
        bus.write_byte_data(addr, 0x07, (int(on) & 0x0F00) >> 8)
        bus.write_byte_data(addr, 0x08, int(off) & 0xFF)
        bus.write_byte_data(addr, 0x09, (int(off) & 0x0F00) >> 8)


