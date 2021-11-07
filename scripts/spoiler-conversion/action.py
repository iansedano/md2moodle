from enum import Enum


class Action_type(Enum):
    process_children = "process_children"
    add_prefix = "add_prefix"
    add_suffix = "add_suffix"


class Action():
    def __init__(self, type, **kwargs):
        self.type = type

        if self.type == Action_type.process_children:
            self.convert_to = kwargs.convert_to
        elif self.type == Action_type.add_prefix or self.type == Action_type.add_suffix:
            self.payload = kwargs.payload
