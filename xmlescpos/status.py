# Implement ESC/POS status request here

from escpos.escpos import Escpos
from escpos.constants import *
from time import sleep

def get_printer_status(printer: Escpos) -> dict:
    status = {}
    response = []

    printer._raw(
        RT_STATUS + b"\x01" + 
        RT_STATUS + b"\x02" + 
        RT_STATUS + b"\x03" + 
        RT_STATUS + b"\x04"
    )
    
    sleep(0.1)

    response = printer._read()

    # If the length is 8, drop the first 4 results
    if len(response) == 8:
        response = response[4:]

    status['printer'] = {
        'status_code': response[0],
        'status_error': not ((response[0] & 147) == 18),
        'online': not bool(response[0] & 0b00001000),
        'recovery': bool(response[0] & 32),
        'drawer_pin_high': bool(response[0] &     0b00000100),
        'paper_feed_on': bool(response[0] & 64),
    }

    status['offline'] = {
        'status_code': response[1],
        'status_error': not ((response[1] & 147) == 18),
        'error': not bool(response[1] & 0b01000000), # TODO: This doesn't seem to change
        'cover_open': bool(response[1] &     0b00000100),
        'paper_feed_on': bool(response[1] &     0b00001000),
        'paper': not bool(response[1] & 0b00100000),
    }

    status['error'] = {
        'status_code': response[2],
        'status_error':not ((response[2] & 147) == 18),
        'unrecoverable': bool(response[2] & 0b00100000),
        'auto_recoverable': not bool(response[2] & 0b01000000),
        'autocutter': bool(response[2] & 0b00001000),
    }

    status['paper'] = {
        'status_code': response[3],
        'status_error': not ((response[3] & 147) == 18),
        'near_end': bool(response[3] & 12),
        'present': not bool(response[3] & 96),
    }

    return status