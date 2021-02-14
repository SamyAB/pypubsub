from typing import List

from pypubsub.base_publisher_subscriber import END_OF_TOPIC_MESSAGE
from pypubsub.data_models.detection_vector import DetectionVector
from pypubsub.base_publisher_subscriber.publisher import Publisher
from pypubsub.base_publisher_subscriber.subscriber import Subscriber
from pypubsub.base_publisher_subscriber.topic import Topic


class SingleShotDetector(Subscriber, Publisher):
    def __init__(self, topics: List[Topic], topic: Topic):
        Subscriber.__init__(self, topics)
        Publisher.__init__(self, topic)

    def process_data(self):
        while True:
            try:
                message = self.topic_connection[0].recv()
                if message == END_OF_TOPIC_MESSAGE:
                    self.publish(END_OF_TOPIC_MESSAGE)
                    break
                dummy_detection_vector_to_publish = DetectionVector(
                    timestamp=message.timestamp,
                    frame_id=message.frame_id,
                    bounding_box=message.bounding_box,
                    prediction_vector=[0.7, 0.2, 0.1]
                )
                self.publish(dummy_detection_vector_to_publish)
            except EOFError:
                break

        self.topic.close()
        self.close()
