from parsing.tokens import Token, Token_type_enum


class Node:
    def __init__(self, construct):
        self.construct = construct
        self.children = []

    def __repr__(self):
        return str(self.construct.name) + str(self.children)


class Parser:
    def parse(self, tokens: list):
        token_generator = (token for token in tokens)
        tree = {"root": Node(Token_type_enum.ROOT)}
        parent_stack = [tree["root"]]

        token = next(token_generator, None)
        adjacent_strings = []
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

            else:
                adjacent_strings.append(token)

            token = next(token_generator, None)
        if len(parent_stack) != 1:
            raise Exception("Parse ended but tree has open nodes")

        return tree
