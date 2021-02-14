# PyPubSub: Simple Inter-Process Communication

A light-weight implementation of an application that handles multiple processes inter-communication using the 
__publish-subscribe messaging pattern__ in Python.

# Demonstration

## Run the demonstration

To showcase the implementation of the pattern, the application can be run in demonstration mode using
the command:

```shell
docker-compose up
```

For this command to work, ensure your current working directory is located at the project root, 
and that you have Docker and Docker Compose installed.

## Understand the demonstration

The demonstration creates a publisher named __MotionDetector__ that sends __MotionVectors__ in the topic __motion_vector__.

A publisher/subscriber named __SingleShotDetector__ subscribes to the topic __motion_vector__ and transforms its content,
in order to publish the result as a __DetectionVector__ in the topic named __detection_vector__.

Lastly, a subscriber named __Logger__ subscribes to both topics, and prints the messages in them on the standard output.

# Development

## Environment and Requirements

The proposed implementation uses only python built-in packages, making it as lightweight as possible.

That being said, if you want to contribute or use this package you may want to install _dev_ requirements.

```shell
pip install .[dev]
```

__Note__: In case the command returns the error

``
no matches found: .[dev]
``

You should try ot escape the brackets

```shell
pip install .\[dev\]
```

## Adapt the PyPubSub to you use case

You may extend the __base_publisher_subscriber__ subpackage to create publishers and subscribers, following 
the examples in the __motion_detection__ subpackage.

To better understand the global usage of the topics' mechanics, please refer to the __main__ module of the package.

Finally, note that publishers can only publish in a single topic, while subscribers can subscribe to multiple topics at once.

# Possible Improvements

- Handle signals SIGTERM and SIGKILL
- Have the topics' reader connections close when their writer counterparts are closed
- Add integration and end-to-end tests
