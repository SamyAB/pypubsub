from unittest.mock import patch, Mock, call

from pypubsub.base_publisher_subscriber import END_OF_TOPIC_MESSAGE
from pypubsub.data_models.bounding_box import BoundingBox
from pypubsub.data_models.detection_vector import DetectionVector
from pypubsub.data_models.motion_vector import MotionVector
from pypubsub.motion_detection.single_shot_detector import SingleShotDetector

TESTED_MODULE = SingleShotDetector.__module__


@patch(f'{TESTED_MODULE}.SingleShotDetector.publish')
def test_process_data_receives_messages_from_topic_subscribe_to_and_publishes_dummy_detection_vector_for_each_one(
        mock_publish):
    # Given
    topic_to_subscribe_to = Mock()
    topic_to_publish_into = Mock()
    single_shot_detector = SingleShotDetector([topic_to_subscribe_to], topic_to_publish_into)
    single_shot_detector.subscribe_to_topics()

    subscription_connection = topic_to_subscribe_to.subscribe.return_value
    motion_vectors = [MotionVector(
        timestamp=10.,
        frame_id=frame_id,
        bounding_box=BoundingBox(x=.2, y=.5, width=20, height=30),
        velocity=((15.5, -6.3), (17.3, 15.5))
    ) for frame_id in range(10)]
    subscription_connection.recv.side_effect = motion_vectors + [END_OF_TOPIC_MESSAGE]

    expected_publish_calls = [
        call(
            DetectionVector(
                timestamp=motion_vector.timestamp,
                frame_id=motion_vector.frame_id,
                bounding_box=motion_vector.bounding_box,
                prediction_vector=[0.7, 0.2, 0.1]
            )
        ) for motion_vector in motion_vectors
    ] + [call(END_OF_TOPIC_MESSAGE)]

    # When
    single_shot_detector.process_data()

    # Then
    mock_publish.assert_has_calls(expected_publish_calls)
