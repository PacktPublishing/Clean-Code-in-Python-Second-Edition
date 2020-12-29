"""Clean Code in Python - Chapter 5: Decorators

Class decorators.

Reimplement the serialization of the events by applying a class decorator.
"""
from dataclasses import dataclass
from datetime import datetime


def hide_field(field) -> str:
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_original(event_field):
    return event_field


class EventSerializer:
    """Apply the transformations to an Event object based on its properties and
    the definition of the function to apply to each field.
    """

    def __init__(self, serialization_fields: dict) -> None:
        """Created with a mapping of fields to functions.

        Example::

        >>> serialization_fields = {
        ...    "username": str.upper,
        ...    "name": str.title,
        ... }

        Means that then this object is called with::

        >>> from types import SimpleNamespace
        >>> event = SimpleNamespace(username="usr", name="name")
        >>> result = EventSerializer(serialization_fields).serialize(event)

        Will return a dictionary where::

        >>> result == {
        ...     "username": event.username.upper(),
        ...     "name": event.name.title(),
        ... }
        True

        """
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        """Get all the attributes from ``event``, apply the transformations to
        each attribute, and place it in a dictionary to be returned.
        """
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.items()
        }


class Serialization:
    """A class decorator created with transformation functions to be applied
    over the fields of the class instance.
    """

    def __init__(self, **transformations):
        """The ``transformations`` dictionary contains the definition of how to
        map the attributes of the instance of the class, at serialization time.
        """
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        """Called when being applied to ``event_class``, will replace the
        ``serialize`` method of this one by a new version that uses the
        serializer instance.
        """

        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime
