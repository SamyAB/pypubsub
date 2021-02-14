from unittest.mock import patch, Mock

import pytest

from pypubsub.base_publisher_subscriber.topic import Topic

TESTED_MODULE = Topic.__module__


@patch(f'{TESTED_MODULE}.Pipe')
def test_subscribe_adds_sender_to_connections_to_listener_and_returns_receiver(mock_pipe):
    # Given
    topic = Topic()

    expected_mock_receiver = Mock()
    expected_mock_sender = Mock()
    mock_pipe.return_value = (expected_mock_receiver, expected_mock_sender)

    # When
    receiver = topic.subscribe()

    # Then
    assert expected_mock_sender in topic.connections_to_listener
    assert receiver == expected_mock_receiver


def test_dispatch_sends_message_to_all_subscribers():
    # Given
    message_to_send = "This is my message"
    topic = Topic()

    first_sub = topic.subscribe()
    second_sub = topic.subscribe()

    # When
    topic.dispatch(message_to_send)

    # Then
    assert first_sub.recv() == message_to_send
    assert second_sub.recv() == message_to_send


def test_dispatch_raises_type_error_if_object_to_dispatch_can_not_be_pickled():
    # Given
    topic = Topic()
    _ = topic.subscribe()

    # Then
    with pytest.raises(TypeError):
        # When
        with open(__file__, 'r') as stream_handler:
            topic.dispatch(stream_handler)


def test_close_topic_should_close_all_the_sender_connections_it_holds():
    # Given
    topic = Topic()
    sender_connection = Mock()
    topic.connections_to_listener = [sender_connection] * 4

    # When
    topic.close()

    # Then
    assert sender_connection.close.call_count == 4
