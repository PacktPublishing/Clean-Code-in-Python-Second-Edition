import unittest

from dip_1 import EventStreamer, DataTargetClient, Event
from dip_2 import object_graph, EventStreamer as EventStreamer2, Syslog


class DoubleClient(DataTargetClient):
    def __init__(self):
        self._sent_count = 0

    def send(self, content: bytes):
        self._sent_count += 1
        return ""


class TestEventStreamer(unittest.TestCase):
    def test_stream(self):
        double_client = DoubleClient()
        event_streamer = EventStreamer(double_client)
        events_data = [
            Event({"transaction": "tx001"}),
            Event({"transaction": "tx002"}),
        ]
        event_streamer.stream(events_data)
        self.assertEqual(double_client._sent_count, len(events_data))

    def test_dependency_injected(self):
        event_streamer = object_graph.provide(EventStreamer2)

        self.assertIsInstance(event_streamer, EventStreamer2)
        self.assertIsInstance(event_streamer.target, Syslog)


if __name__ == "__main__":
    unittest.main()
