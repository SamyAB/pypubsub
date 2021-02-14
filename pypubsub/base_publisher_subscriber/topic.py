import logging
from multiprocessing import Pipe
from multiprocessing.connection import Connection
from typing import List


class Topic:
    def __init__(self):
        self.connections_to_listener: List[Connection] = []

    def dispatch(self, obj: any) -> None:
        for connection_to_listener in self.connections_to_listener:
            try:
                connection_to_listener.send(obj)
            except TypeError:
                logging.error('Message containing could not be dispatched')
                raise TypeError

    def subscribe(self) -> Connection:
        receiver, sender = Pipe(duplex=False)
        self.connections_to_listener.append(sender)

        return receiver

    def close(self) -> None:
        for connection_to_listener in self.connections_to_listener:
            connection_to_listener.close()
