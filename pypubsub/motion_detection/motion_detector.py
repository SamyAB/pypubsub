import time

from pypubsub.base_publisher_subscriber import END_OF_TOPIC_MESSAGE
from pypubsub.data_models.bounding_box import BoundingBox
from pypubsub.data_models.motion_vector import MotionVector
from pypubsub.base_publisher_subscriber.publisher import Publisher
from pypubsub.base_publisher_subscriber.topic import Topic


class MotionDetector(Publisher):
    def __init__(self, topic: Topic):
        super().__init__(topic)

    def process_data(self) -> None:
        for frame_id in range(10):
            dummy_motion_vector_to_publish = MotionVector(
                timestamp=time.time(),
                frame_id=frame_id,
                bounding_box=BoundingBox(x=.2, y=.5, width=20, height=30),
                velocity=((15.5, -6.3), (17.3, 15.5))
            )
            self.publish(dummy_motion_vector_to_publish)
            time.sleep(1)
        self.publish(END_OF_TOPIC_MESSAGE)
        self.topic.close()
