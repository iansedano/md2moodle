"""Will apply the actions from the constructs to the parsed tree
"""

from parsing.parser import Node
import constructs.elements


def process_tree(tree):
    print(tree)
    root: Node = tree["root"]

    def process_branch(branch):

        children: list = branch.children

        children_generator = (child for child in children)

        current_child: Node = next(children_generator, None)
        print(current_child)

        while current_child is not None:
            if isinstance(current_child, Node):
                construct = current_child.construct.actions
                print(construct)
                # process_branch(current_child)
            current_child: Node = next(children_generator, None)

    process_branch(root)
