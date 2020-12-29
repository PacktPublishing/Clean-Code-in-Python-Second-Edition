"""Clean Code in Python - Chapter 6: Descriptors

> Using descriptors instead of class decorators

"""
from dataclasses import dataclass
from datetime import datetime
from functools import partial
from typing import Any, Callable


class BaseFieldTransformation:
    """Base class to define descriptors that convert values."""

    def __init__(self, transformation: Callable[[Any, str], str]) -> None:
        self._name = None
        self.transformation = transformation

    def __get__(self, instance, owner):
        if instance is None:
            return self
        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


ShowOriginal = partial(BaseFieldTransformation, transformation=lambda x: x)
HideField = partial(
    BaseFieldTransformation, transformation=lambda x: "**redacted**"
)
FormatTime = partial(
    BaseFieldTransformation,
    transformation=lambda ft: ft.strftime("%Y-%m-%d %H:%M"),
)


@dataclass
class LoginEvent:

    username: str = ShowOriginal()  # type: ignore
    password: str = HideField()  # type: ignore
    ip: str = ShowOriginal()  # type: ignore
    timestamp: datetime = FormatTime()  # type: ignore

    def serialize(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,
        }
