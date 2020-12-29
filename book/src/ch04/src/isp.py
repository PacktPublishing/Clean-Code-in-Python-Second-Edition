"""Clean Code in Python - Second edition
Chapter 04 - The SOLID Principles

ISP: Interface Segregation Principle
"""

from abc import ABCMeta, abstractmethod


class XMLEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_xml(xml_data: str):
        """Parse an event from a source in XML representation."""


class JSONEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_json(json_data: str):
        """Parse an event from a source in JSON format."""


class EventParser(XMLEventParser, JSONEventParser):
    """An event parser that can create an event from source data either
    in XML or JSON format.
    """

    def from_xml(xml_data):
        pass

    def from_json(json_data: str):
        pass
