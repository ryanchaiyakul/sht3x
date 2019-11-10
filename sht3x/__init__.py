from . import sht3x

def get_device(config: str):
    return sht3x.SHT3x(config)