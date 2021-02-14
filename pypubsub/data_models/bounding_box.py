from dataclasses import dataclass


@dataclass
class BoundingBox:
    x: float
    y: float
    width: float
    height: float
