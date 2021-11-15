from enum import Enum


class Action_type(Enum):
    process_children = "process_children"
    add_prefix = "add_prefix"
    add_suffix = "add_suffix"


class Action():
    def __init__(self, type: Action_type, payload: str):
        self.type = type
        self.payload = payload
