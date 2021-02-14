from dataclasses import dataclass
from typing import Tuple

from pypubsub.data_models.bounding_box import BoundingBox


@dataclass
class MotionVector:
    timestamp: float
    frame_id: int
    bounding_box: BoundingBox
    velocity: Tuple[Tuple[float, float], Tuple[float, float]]
