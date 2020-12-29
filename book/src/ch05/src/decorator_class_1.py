"""Clean Code in Python - Chapter 5: Decorators

> Class decorators.
"""
from datetime import datetime
from dataclasses import dataclass


class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username": self.event.username,
            "password": "**redacted**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d %H:%M"),
        }


@dataclass
class LoginEvent:
    SERIALIZER = LoginEventSerializer

    username: str
    password: str
    ip: str
    timestamp: datetime

    def serialize(self) -> dict:
        return self.SERIALIZER(self).serialize()
