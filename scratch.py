class RIM:
    def __init__(self, partnumber: str):
        self.part_number = partnumber
        self.slot_cards = {}

class Card:
    def __init__(self, iotype: str):
        self.io_type = iotype
        self.max_channel_count = self._get_channel_count(iotype)
        self.channels = {}

    def _get_channel_count(self, iotype: str):
        if 'x' in iotype:
            return iotype.split('x')[0]
        else:
            return 'unknown'

def get_channel_from_pin(pin_number: str, channel_count: str) -> str:
    if channel_count != 'unknown':
        pin = int(pin_number)
        count = int(channel_count)

        if count == 4:
            if pin < 1 or pin > 16:
                raise ValueError("Invalid pin for 4-channel card (pins 1–16)")
            channel = ((pin - 1) // 4) + 1

        elif count == 8:
            if pin < 1 or pin > 16:
                raise ValueError("Invalid pin for 8-channel card (pins 1–16)")
            channel = ((pin - 1) // 2) + 1

        elif count == 16:
            if pin < 1 or pin > 16:
                raise ValueError("Invalid pin for 16-channel card (pins 1–16)")
            channel = pin

        else:
            channel = ''
            raise ValueError(f"Unsupported channel count: {count}")

        return str(channel)



import csv

filepath = "V:\\ChristianJ\\IOMAPs\\12-202256-01_ilk_io_map 1.csv"
iomap_raw = {}
rims = {}

with open(filepath, 'r', newline='') as iomap_file:
    iomap_raw = csv.DictReader(iomap_file)

    for row in iomap_raw:
        rims.setdefault(f'RIM {row["rim"]}', RIM(partnumber=row["part_number"]))
        if int(row["slot"]) > 0:
            rim = rims[f'RIM {row["rim"]}']
            if f'Slot {row["slot"]}' not in rims[f'RIM {row["rim"]}'].slot_cards:
                rim.slot_cards[f'Slot {row["slot"]}'] = Card(iotype=row['io_type'])
            slot = rim.slot_cards[f'Slot {row["slot"]}']
            chan_no = get_channel_from_pin(row["pin"], slot.max_channel_count)
            if f'Channel {chan_no}' not in slot.channels:
                slot.channels[f'Channel {chan_no}'] = row['signal_name']
            channel = slot.channels[f'Channel {chan_no}']

for rim in rims:
    print(f'{rim}:\t{rims[rim].part_number}')
    for card in rims[rim].slot_cards:
        print(f'\t{card}:\t{rims[rim].slot_cards[card].io_type}')
        '''
        for channel in rims[rim].slot_cards[card].channels:
            print(f'\t\t{channel}:\t{rims[rim].slot_cards[card].channels[channel]}')
        '''
