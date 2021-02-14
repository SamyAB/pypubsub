from multiprocessing.connection import Connection
from typing import List

from pypubsub.base_publisher_subscriber.topic import Topic


class Subscriber:
    def __init__(self, topics: List[Topic]):
        self.topics_subscribed_to: List[Topic] = topics
        self.topic_connection: List[Connection] = []

    def subscribe_to_topics(self) -> None:
        for topic_to_subscribe_to in self.topics_subscribed_to:
            self.topic_connection.append(topic_to_subscribe_to.subscribe())

    def close(self) -> None:
        for topic_connection in self.topic_connection:
            topic_connection.close()
