from dataclasses import dataclass
from enum import Enum, auto
import re

from pprint import pp


class Token_enum(Enum):
    SPOILER = auto()
    NOTE = auto()
    ALERT = auto()
    TAG = auto()


class Token_type_enum(Enum):
    OPEN_TAG = auto()
    CLOSE_TAG = auto()
    INLINE = auto()


class Token:
    def __init__(self, name: Token_enum, token_type: Token_type_enum, pattern: str):
        self.name, self.token_type = name, token_type
        self.pattern = re.compile(pattern)

    def __repr__(self):
        return (f"{self.name}, {self.token_type}, {self.pattern}")

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.token_type == other.token_type
        )

    def match(self, string, flags=0):
        return re.match(self.pattern, string, flags)
