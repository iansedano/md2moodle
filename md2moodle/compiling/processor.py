"""Will apply the actions from the constructs to the parsed tree
"""

# md2moodle imports
import md2moodle.constructs.elements
from md2moodle.constructs.action import Action, Action_type
from md2moodle.debug import p
from md2moodle.parsing.parser import Node
from md2moodle.parsing.tokens import Token_type_enum


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
