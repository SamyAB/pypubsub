from unittest.mock import Mock

from pypubsub.base_publisher_subscriber.publisher import Publisher


def test_publish_should_dispatch_object_in_the_publishers_topic():
    # Given
    mock_topic = Mock()
    publisher = Publisher(mock_topic)
    object_to_send = "Message"

    # When
    publisher.publish(object_to_send)

    # Then
    mock_topic.dispatch.assert_called_once_with(object_to_send)
