from virtualnodes import *
from virtualtests import *
from dataclasses import dataclass
from typing import List


@dataclass
class FieldConnect:
    connector: str
    pin: str


@dataclass
class Channel:
    name: str
    rim: str
    slot: str
    card_pin: str
    io_type: str
    connect: FieldConnect

    @property
    def channel_number(self) -> int:
        if self.total_channels == 16:
            return self.pin_number
        elif self.total_channels == 8:
            return (self.pin_number + 1) // 2
        else:
            raise ValueError("Unsupported channel count (only 8 or 16 allowed)")



class Card:
    def __init__(self):
        self.part_number = ''
        self.io_type = ''
        self.max_channels = ''
        self.channels = []


class Controller:
    def __init__(self):
        self.part_number = ''
        self.description = ''
        self.product_type = ''

class Rim(Controller):
    def __init__(self):
        super().__init__()
        self.rimport = ''
        self.slot_cards= []

class Rcm(Controller):
    def __init__(self):
        super().__init__()
        self.cm_fabric: ''
        self.firmware: ''
        self.rims: []

class Fusion(Rcm):
    def __init__(self):
        super().__init__()
        self.slot_cards: []

class System:
    def __init__(self):
        self.customer = ''
        self.system_name = ''
        self.controllers = {}
