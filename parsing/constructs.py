from abc import ABCMeta, abstractmethod

from parsing.tokens import Token


class Element(metaclass=ABCMeta):
    @abstractmethod
    def get_tokens(self) -> list[Token]:
        raise NotImplementedError


class Default_element(Element):
    def __init__(self, name, start_tag: Token, end_tag: Token, *, actions):
        self.name = name
        self.start_tag = start_tag
        self.end_tag = end_tag
        self.actions = actions

    def get_tokens(self):
        return [self.start_tag, self.end_tag]


class Inline_element(Element):
    def __init__(self, name, token: Token, *, actions):
        self.name = name
        self.token = token
        self.actions = actions

    def get_tokens(self):
        return [self.token]
