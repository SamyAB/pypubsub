import logging
from unittest.mock import Mock, patch, call

from pypubsub.base_publisher_subscriber import END_OF_TOPIC_MESSAGE
from pypubsub.motion_detection.logger import Logger

TESTED_MODULE = Logger.__module__


def test_log_top_messages_stops_does_not_log_anything_if_first_message_is_end_of_topic_message(caplog):
    # Given
    topic_connection = Mock()
    topic_connection.recv.return_value = END_OF_TOPIC_MESSAGE

    # When
    with caplog.at_level(logging.INFO):
        Logger.log_topic_messages(topic_connection)

    # Then
    assert len(caplog.records) == 0


def test_log_topic_messages_logs_all_the_messages_before_the_end_of_topic_message(caplog):
    # Given
    topic_connection = Mock()
    messages = ['First Message', 'Second Message', END_OF_TOPIC_MESSAGE]
    topic_connection.recv.side_effect = messages

    # When
    with caplog.at_level(logging.INFO):
        Logger.log_topic_messages(topic_connection)

    # Then
    for message in messages[:-1]:
        assert message in caplog.text


@patch(f'{TESTED_MODULE}.Logger.log_topic_messages')
def test_process_data_should_run_the_log_topic_messages_method_of_each_of_the_topics_subscribed_to(
        mock_log_topic_messages):
    # Given
    first_topic = Mock()
    second_topic = Mock()
    logger = Logger([first_topic, second_topic])
    logger.subscribe_to_topics()

    expected_log_topic_messages_calls = [
        call(first_topic.subscribe.return_value),
        call(second_topic.subscribe.return_value),
    ]

    # When
    logger.process_data()

    # Then
    mock_log_topic_messages.assert_has_calls(expected_log_topic_messages_calls)
