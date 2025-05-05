from dataclasses import dataclass
from typing import List, Optional


@dataclass
class vNode:
    name: str
    source: Optional["vNode"] = None
    next: Optional["vNode"] = None


class NodeCard(vNode):
    io_type: str
    mb_position: str
    card: Optional["vCard"] = None


class NodeFC(vNode):
    connector: str
    pins: List[str]
    card: Optional["vCard"] = None


@dataclass
class vChannel:
    name: str
    node: List[vNode]


@dataclass
class vCard:
    part_number: str
    io_type: str
    max_channels: str
    channels: List[vChannel]

@dataclass
class vController:
    part_number: str
    serial_number: str
    description: str
    product_type: str
    main_customer: str


@dataclass
class vRim(vController):
    rim_fabric: str
    slot_cards: List[vCard]


@dataclass
class vFusion(vController):
    rim_fabric: str
    cm_fabric: str
    firmware: str
    slot_cards: List[str]
    rims: List[vRim]

@dataclass
class vSystem:
    customer: str
    tool_name: str
    rim_1: vController
    rim_2: vController
    rim_3: vController
    rim_4: vController
    rim_5: vController
