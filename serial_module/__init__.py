from serial import EIGHTBITS, PARITY_NONE, STOPBITS_ONE

serial_port_args = {
    'port': None,
    'baundrate': 9600,
    'bytesize': EIGHTBITS,
    'parity': PARITY_NONE,
    'stopbits': STOPBITS_ONE,
    'xonxoff': False
}
