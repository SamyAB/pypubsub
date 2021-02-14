import logging
from multiprocessing.pool import ThreadPool
from multiprocessing.connection import Connection
from typing import List

from pypubsub.base_publisher_subscriber import END_OF_TOPIC_MESSAGE
from pypubsub.base_publisher_subscriber.subscriber import Subscriber
from pypubsub.base_publisher_subscriber.topic import Topic


class Logger(Subscriber):
    def __init__(self, topics: List[Topic]):
        super().__init__(topics)

    def process_data(self) -> None:
        with ThreadPool(len(self.topic_connection)) as thread_pool:
            thread_pool.map(Logger.log_topic_messages, self.topic_connection)

        logging.info('No more data to log')
        self.close()

    @staticmethod
    def log_topic_messages(topic_connection: Connection) -> None:
        while True:
            try:
                message = topic_connection.recv()
                if message == END_OF_TOPIC_MESSAGE:
                    break
                logging.info(message)
            except EOFError:
                break
