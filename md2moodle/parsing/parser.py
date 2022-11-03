# md2moodle imports
from md2moodle.parsing.tokens import Token, Token_type_enum


class ParsingError(Exception):
    pass

class Node:
    """Generic class to build abstract syntax tree"""

    def __init__(self, construct):
        self.construct = construct
        self.children = []

    def __repr__(self):
        return str(self.construct.name) + str(self.children)


def parse(tokens: list):
    """Parses a list of tokens and builds an abstract syntax tree"""
    token_generator = iter(tokens)
    tree = {"root": Node(Token_type_enum.ROOT)}
    parent_stack = [tree["root"]]

    token = next(token_generator, None)
    adjacent_strings: list[Token] = []
    while token is not None:
        if isinstance(token, Token):
            parent_stack[-1].children.append("\n".join(adjacent_strings))
            adjacent_strings = []

            if token.token_type == Token_type_enum.START_TAG:
                new_node = Node(token.parent)
                parent_stack[-1].children.append(new_node)
                parent_stack.append(new_node)
            elif token.token_type == Token_type_enum.END_TAG:
                parent_stack.pop(-1)
            elif token.token_type == Token_type_enum.PREFIX:
                new_node = Node(token.parent)
                new_node.children.append(next(token_generator, None))
                parent_stack[-1].children.append(new_node)

        else:
            adjacent_strings.append(token)

        token = next(token_generator, None)
    if len(parent_stack) != 1:
        raise ParsingError("Open nodes or closing unopened node")

    parent_stack[-1].children.append("\n".join(adjacent_strings))

    return tree
