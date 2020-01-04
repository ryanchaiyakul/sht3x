import stickytoe_device
import time
import smbus2
import json


class SHT3x(stickytoe_device.DEVICE.I2C):

        def __init__(self, config: dict):
                super().__init__(config)
                self.smbus = smbus2.SMBus(self.bus)

        def execute(self, payload: str):
                cmd_dict = json.loads(payload)  # ValueError handled by caller
                
                self.smbus.write_i2c_block_data(self.addr, 0x2C, [0x06])

                time.sleep(0.5)

                # SHT30 address, 0x44(68)
                # Read data back from 0x00(00), 6 bytes
                # cTemp MSB, cTemp LSB, cTemp CRC, Humididty MSB, Humidity LSB, Humidity CRC
                data = self.smbus.read_i2c_block_data(self.addr, 0x00, 6)

                # Convert the data
                
                temp = ((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45
                humidity = None
                if cmd_dict["temperature"]:
                    temp = temp * 1.8 + 32
                if cmd_dict["humidity"]:
                    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

                if humidity is None:
                    return json.dumps({"temperature":temp})
                return json.dumps({"temperature":temp, "humidity":humidity})
