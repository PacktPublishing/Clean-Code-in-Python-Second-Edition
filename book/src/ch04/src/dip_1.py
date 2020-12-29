"""Clean Code in Python - Second edition
Chapter 04 - The SOLID Principles

DIP: Dependency Inversion Principle

Demo of the dependency injection section.
"""
from __future__ import annotations

import json

from abc import ABCMeta, abstractmethod


class Event:
    def __init__(self, content: dict) -> None:
        self._content = content

    def serialise(self):
        return json.dumps(self._content)


class DataTargetClient(metaclass=ABCMeta):
    @abstractmethod
    def send(self, content: bytes):
        """Send raw content to a particular target."""


class Syslog(DataTargetClient):
    def send(self, content: bytes):
        return f"[{self.__class__.__name__}] sent {len(content)} bytes"


class EventStreamer:
    def __init__(self, target: DataTargetClient):
        self.target = target

    def stream(self, events: list[Event]) -> None:
        for event in events:
            self.target.send(event.serialise())
