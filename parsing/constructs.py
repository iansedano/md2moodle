from abc import ABCMeta, abstractmethod

from parsing.tokens import Token


class Element(metaclass=ABCMeta):
    @abstractmethod
    def get_tokens(self) -> list[Token]:
        raise NotImplementedError


class Default_element(Element):
    def __init__(self, *, name: str, start_tag: Token, end_tag: Token, actions: dict):
        self.name = name
        self.start_tag = start_tag
        self.end_tag = end_tag
        self.actions = actions

    def get_tokens(self):
        return [self.start_tag, self.end_tag]


class Prefix_inline_element(Element):
    def __init__(self, *, name: str, prefix: Token, actions: dict):
        self.name = name
        self.prefix = prefix
        self.actions = actions

    def get_tokens(self):
        return [self.token]
