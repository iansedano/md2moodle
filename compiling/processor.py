"""Will apply the actions from the constructs to the parsed tree
"""

from parsing.parser import Node
from parsing.tokens import Token_type_enum
import constructs.elements
from constructs.action import Action, Action_type

from debug import p


def process_tree(tree):
    root: Node = tree["root"]

    def process_branch(branch):
        children: list = branch.children
        children_generator = (child for child in children)
        current_child: Node = next(children_generator, None)
        text_buffer = []

        while current_child is not None:
            if isinstance(current_child, Node):
                actions = sorted(current_child.construct.actions, key=lambda a: a.type)

                for action in actions:
                    action.execute(current_child)

                process_branch(current_child)

            current_child: Node = next(children_generator, None)

    process_branch(root)

    return root
