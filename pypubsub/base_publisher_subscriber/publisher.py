from pypubsub.base_publisher_subscriber.topic import Topic


class Publisher:
    def __init__(self, topic: Topic):
        self.topic: Topic = topic

    def publish(self, obj) -> None:
        self.topic.dispatch(obj)
