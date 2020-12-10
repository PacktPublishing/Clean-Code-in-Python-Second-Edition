"""Clean Code in Python - Chapter 1: Introduction, Tools, and Formatting

> Tools for type hinting: examples
"""
from __future__ import annotations

import logging
from typing import Iterable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def broadcast_notification(message: str, relevant_user_emails: Iterable[str]):
    for email in relevant_user_emails:
        logger.info("Sending %r to %r", message, email)


broadcast_notification("welcome", ["user1@domain.com", "user2@domain.com"])
broadcast_notification("welcome", "user1@domain.com")
