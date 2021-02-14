from unittest.mock import patch, call, Mock

from pypubsub.base_publisher_subscriber import END_OF_TOPIC_MESSAGE
from pypubsub.data_models.bounding_box import BoundingBox
from pypubsub.data_models.motion_vector import MotionVector
from pypubsub.motion_detection.motion_detector import MotionDetector

TESTED_MODULE = MotionDetector.__module__


@patch(f'{TESTED_MODULE}.time.time', return_value=10.)
@patch(f'{TESTED_MODULE}.time.sleep')
@patch(f'{TESTED_MODULE}.MotionDetector.publish')
def test_process_data_publishes_dummy_motion_vector_10_times_and_end_of_topic_message(mock_publish, mock_sleep, _):
    # Given
    topic = Mock()
    motion_vector = MotionDetector(topic)

    dummy_motion_vectors = [MotionVector(
        timestamp=10.,
        frame_id=frame_id,
        bounding_box=BoundingBox(x=.2, y=.5, width=20, height=30),
        velocity=((15.5, -6.3), (17.3, 15.5))
    ) for frame_id in range(10)]
    expected_publish_calls = [
        call(dummy_motion_vector) for dummy_motion_vector in dummy_motion_vectors] + [call(END_OF_TOPIC_MESSAGE)]

    # When
    motion_vector.process_data()

    # Then
    assert mock_sleep.call_count == 10
    mock_publish.assert_has_calls(expected_publish_calls)
