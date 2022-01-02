from enum import Enum
import re

from pprint import pp


class Token_type_enum(Enum):
    START_TAG = "start_tag"
    END_TAG = "end_tag"
    PREFIX = "prefix"
    ROOT = "root"


class Token:
    def __init__(self, *, token_type: Token_type_enum, pattern: str):
        self.token_type = token_type
        self.precompiled_pattern = pattern
        self.pattern = re.compile(pattern)

    def add_parent(self, parent):
        self.parent = parent

    def __eq__(self, other):
        return (
            self.token_type == other.token_type
            and self.precompiled_pattern == other.precompiled_pattern
        )

    def match(self, string, flags=0):
        return re.match(self.pattern, string.strip(), flags)
