from tokens import Token, Token_type_enum


class Node():
    def __init__(self, token_name):
        self.token_name = token_name
        self.children = []

    def __repr__(self):
        return str(self.token_name) + str(self.children)


class Parser():
    def parse(self, lines: list):
        line_generator = (line for line in lines)
        tree = {"root": Node(Token_enum.ROOT)}
        parent_stack = [tree["root"]]

        line = next(line_generator, None)
        while line is not None:
            if isinstance(line, Token):
                if line.token_type == Token_type_enum.START_TAG:
                    new_node = Node(line.name)
                    parent_stack[-1].children.append(new_node)
                    parent_stack.append(new_node)

                elif line.token_type == Token_type_enum.END_TAG:
                    parent_stack.pop(-1)

            else:
                parent_stack[-1].children.append(line)

            line = next(line_generator, None)
        if len(parent_stack) != 1:
            raise Exception("Parse ended but tree has open nodes")

        return tree
