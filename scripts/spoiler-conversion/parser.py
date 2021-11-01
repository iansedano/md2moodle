from tokens import Token, Token_enum, Token_type_enum


class Node():
    def __init__(self, token_name: Token_enum):
        self.token_name = token_name
        self.children = []

    def __repr__(self):
        return str(self.token_name) + str(self.children)


class Parser():
    def parse(self, lines: list):
        line_generator = (line for line in lines)
        print("line gen", line_generator)
        tree = {"root": Node(Token_enum.ROOT)}
        parent_stack = [tree["root"]]

        line = next(line_generator, None)
        print("first line", line)
        while line is not None:
            print("line from parser", line)
            if isinstance(line, Token):
                if line.token_type == Token_type_enum.OPEN_TAG:
                    new_node = Node(line.name)
                    parent_stack[-1].children.append(new_node)
                    parent_stack.append(new_node)

                elif line.token_type == Token_type_enum.CLOSE_TAG:
                    parent_stack.pop(-1)

            else:
                parent_stack[-1].children.append(line)

            line = next(line_generator, None)
        if len(parent_stack) != 1:
            raise Exception(
                "not at root level...tree has open nodes, parent stack has more than root")

        return tree
