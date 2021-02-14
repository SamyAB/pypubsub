from dataclasses import dataclass
from typing import List

from pypubsub.data_models.bounding_box import BoundingBox


@dataclass
class DetectionVector:
    timestamp: float
    frame_id: int
    bounding_box: BoundingBox
    prediction_vector: List[float]
