from copy import deepcopy

import virtualfusion as vfusion
import json

class Preloader:
    def __init__(self, arg: str):
        self.sysdef = self.__load_sysdef(arg)
        self.system = self.__get_system()

    def get_system(self):
        return deepcopy(self.system)

    def __load_sysdef(self, filepath: str):
        json_data = None
        try:
            with open(filepath, 'r') as systemdef_json:
                json_data = json.load(systemdef_json)
        except Exception as e:
            print(e)
        return json_data

    def __load_cards(self, slots: list):
        card_xref = {}
        try:
            with open('io_card_def.json') as f:
                card_xref = json.load(f)
        except Exception as e:
            print(e)
        cards = []
        for slot in slots:
            new_card = vfusion.Card()
            new_card.part_number = slot['pn']
            new_card.io_type = card_xref[slot['id']]['io_type']
            new_card.max_channels = card_xref[slot['id']]['desc'].split('x')[0]
            cards.append(new_card)
        return cards

    def __get_system(self):
        rims = {}
        for rim in self.sysdef['rims']:
            if rim['pn']:
                if 0 < rim['port_id'] < 5:
                    new_rim = vfusion.Rim()
                    new_rim.part_number = rim['pn']
                    new_rim.description = rim['desc']
                    new_rim.product_type = rim['type']
                    new_rim.rimport = str(rim['port_id'])
                    new_rim.slot_cards = self.__load_cards(rim['slots'])
                    rims[str(rim['port_id'])] = new_rim
                elif rim['port_id'] == 5:
                    new_cm = vfusion.Fusion()
                    new_cm.part_number = rim['pn']
                    new_cm.description = rim['desc']
                    new_cm.product_type = rim['type']
                    new_cm.cm_fabric = self.sysdef['cm_fpga_fabric_version']
                    new_cm.firmware = self.sysdef['firmware_version']
                    new_cm.rims = list(rims.values())
                    new_cm.slot_cards = self.__load_cards(rim['slots'])
                    rims[str(rim['port_id'])] = new_cm
        return rims