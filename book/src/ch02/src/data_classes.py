"""Clean code in Python - Second edition
Chapter 2: Data classes
"""

from typing import List
from dataclasses import dataclass, field


R = 26


@dataclass
class RTrieNode:
    size = R
    value: int
    next_: List["RTrieNode"] = field(
        default_factory=lambda: [None] * R
    )

    def __post_init__(self):
        if len(self.next_) != self.size:
            raise ValueError(f"Invalid length provided for next list")
