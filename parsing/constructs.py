from abc import ABCMeta, abstractmethod

from tokens import Token


class Element(metaclass=ABCMeta):
    @abstractmethod
    def get_tokens(self) -> list[Token]:
        raise NotImplementedError


class Default_element(Element):
    def __init__(self, name, start_tag: Token, end_tag: Token):
        self.name = name
        self.start_tag = start_tag
        self.end_tag = end_tag

    def get_tokens(self):
        return [self.start_tag, self.end_tag]


class Inline_element(Element):
    def __init__(self, name, token: Token):
        self.name = name
        self.token = token

    def get_tokens(self):
        return [self.token]
