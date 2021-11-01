from tokens import Token, Token_enum, Token_type_enum
import abc


class Element(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_tokens(self) -> list[Token]:
        raise NotImplementedError


class Tag_element(Element):
    def __init__(self, open_tag: Token, close_tag: Token):
        if open_tag.name == close_tag.name:
            self.name = open_tag.name
        else:
            raise TypeError
        self.open_tag = open_tag
        self.close_tag = close_tag

    def get_tokens(self):
        return [self.open_tag, self.close_tag]


class Inline_element(Element):
    def __init__(self, token: Token):
        self.token = token

    def get_tokens(self):
        return [self.token]


constructs = [
    Tag_element(
        Token(Token_enum.SPOILER,
              Token_type_enum.OPEN_TAG, r"\[SPOILER\]"),
        Token(Token_enum.SPOILER,
              Token_type_enum.CLOSE_TAG, r"\[\/SPOILER\]")
    ),
    Tag_element(
        Token(Token_enum.NOTE,
              Token_type_enum.OPEN_TAG, r"\[NOTE\]"),
        Token(Token_enum.NOTE,
              Token_type_enum.CLOSE_TAG, r"\[\/NOTE\]")
    ),
    Tag_element(
        Token(Token_enum.ALERT,
              Token_type_enum.OPEN_TAG, r"\[ALERT\]"),
        Token(Token_enum.ALERT,
              Token_type_enum.CLOSE_TAG, r"\[\/ALERT\]")
    ),
    Inline_element(
        Token(Token_enum.TAG,
              Token_type_enum.INLINE, r"@#\w+")
    )
]
