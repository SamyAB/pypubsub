import logging
import sys
from multiprocessing import Process
from typing import Tuple

from pypubsub.base_publisher_subscriber.topic import Topic
from pypubsub.motion_detection.logger import Logger
from pypubsub.motion_detection.motion_detector import MotionDetector
from pypubsub.motion_detection.single_shot_detector import SingleShotDetector


def init_logger() -> None:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def init_application() -> Tuple[Process, Process, Process]:
    motion_vector_topic = Topic()
    detection_vector_topic = Topic()

    motion_detector = MotionDetector(motion_vector_topic)
    single_shot_detector = SingleShotDetector(topics=[motion_vector_topic], topic=detection_vector_topic)
    topics_logger = Logger([motion_vector_topic, detection_vector_topic])

    topics_logger.subscribe_to_topics()
    single_shot_detector.subscribe_to_topics()

    logger_process = Process(target=topics_logger.process_data)
    motion_detector_process = Process(target=motion_detector.process_data)
    single_shot_detector_process = Process(target=single_shot_detector.process_data)
    return logger_process, motion_detector_process, single_shot_detector_process


if __name__ == '__main__':
    init_logger()

    app_processes = init_application()

    for process in app_processes:
        process.start()

    for process in app_processes:
        process.join()
