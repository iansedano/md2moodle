"""Will apply the actions from the constructs to the parsed tree
"""

from parsing.parser import Node
import constructs.elements
from constructs.action import Action


def process_tree(tree):
    print(tree)
    root: Node = tree["root"]

    def process_branch(branch):

        children: list = branch.children

        children_generator = (child for child in children)

        current_child: Node = next(children_generator, None)
        print(current_child)

        while current_child is not None:
            print(current_child)
            if isinstance(current_child, Node):
                actions = current_child.construct.actions

                for action in actions:
                    print(action.type)
                # process_branch(current_child)
            current_child: Node = next(children_generator, None)

    process_branch(root)
