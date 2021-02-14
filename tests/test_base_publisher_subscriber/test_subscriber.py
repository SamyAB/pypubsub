from unittest.mock import Mock

from pypubsub.base_publisher_subscriber.subscriber import Subscriber


def test_subscribe_to_topics_runs_topics_subscribe_for_each_topic_to_subscribe_to_and_stores_the_receiver():
    # Given
    mock_topic = Mock()
    number_of_topics = 3
    topics = [mock_topic] * number_of_topics
    subscriber = Subscriber(topics)

    mock_receiver = mock_topic.subscribe.return_value
    expected_mock_connections = [mock_receiver] * number_of_topics

    # When
    subscriber.subscribe_to_topics()

    # Then
    assert mock_topic.subscribe.call_count == number_of_topics
    assert subscriber.topic_connection == expected_mock_connections


def test_close_should_call_close_on_all_connection_stored_in_the_subscriber():
    # Given
    mock_connection = Mock()
    subscriber = Subscriber([])
    number_of_connections = 4
    subscriber.topic_connection = [mock_connection] * number_of_connections

    # When
    subscriber.close()

    # Then
    assert mock_connection.close.call_count == number_of_connections
