import virtualfusion as vfusion
import virtualnodes as vnodes
import virtualtests as vtests
from preloader import Preloader
from virtualfusion import FieldConnect

iomap_filepath = ''

headers = {"designation": 0,
           "title": 1,
           "connector_pin": 2,
           "signal_name": 3,
           "io_type": 4,
           "rim": 5,
           "slot": 6,
           "pin": 7,
           "io_id": 8,
           "rim_name": 9,
           "part_number": 10,
           "ecat_id": 11,
           "ecat_offset": 12,
           "ecat_length": 13}

def get_channel_count(io_type: str) -> str:
    return io_type.split('x')[0]

def get_channel_number(pin_number: int, total_channels: int) -> int:
    if total_channels == 16:
        return pin_number
    elif total_channels == 8:
        return (pin_number + 1) // 2
    else:
        raise ValueError("Unsupported channel count (only 8 or 16 supported)")

iomap = []

system_preloader = Preloader(iomap_filepath)
my_system = system_preloader.get_system()

for row in iomap:
    if int(row[headers['slot']]) >= 0:
        new_channel = vfusion.Channel(name=row[headers['signal_name']],
                                      rim=row[headers['rim']],
                                      slot=row[headers['slot']],
                                      card_pin=row[headers['pin']],
                                      io_type=row[headers['io_type']].split('x')[1],
                                      connect=FieldConnect(connector=row[headers['designation']],
                                                           pin=row[headers['connector_pin']]
                                                           )
                                      )
        # either use preloader or load cards into controllers here

