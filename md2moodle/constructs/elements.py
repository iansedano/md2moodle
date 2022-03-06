from abc import ABCMeta, abstractmethod

from md2moodle.parsing.tokens import Token
from md2moodle.constructs.action import Action, Action_type


class Meta_element(metaclass=ABCMeta):
    @abstractmethod
    def get_tokens(self) -> list[Token]:
        raise NotImplementedError


class Element:
    def __init__(self, name: str, actions: dict):
        self.name = name
        self.actions = self.build_actions(actions)

    def build_actions(self, actions: dict):
        output = []
        for type, payload in actions.items():
            output.append(Action(Action_type[type], payload))
        return output


class Default_element(Meta_element, Element):
    def __init__(self, *, name: str, start_tag: Token, end_tag: Token, actions: dict):
        super().__init__(name, actions)
        self.start_tag = start_tag
        self.end_tag = end_tag

    def get_tokens(self):
        return [self.start_tag, self.end_tag]


class Prefix_inline_element(Meta_element, Element):
    def __init__(self, *, name: str, prefix: Token, actions: dict):
        super().__init__(name, actions)
        self.prefix = prefix

    def get_tokens(self):
        return [self.prefix]
