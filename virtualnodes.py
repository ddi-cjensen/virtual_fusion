from virtualfusion import *
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    name: str
    source: Optional["Node"] = None
    next: Optional["Node"] = None


class NodeCard(Node):
    io_type: str
    mb_position: str
    card: Optional["Card"] = None


class NodeFC(Node):
    connector: str
    pins: List[str]
    card: Optional["Card"] = None