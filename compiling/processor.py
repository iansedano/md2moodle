"""Will apply the actions from the constructs to the parsed tree
"""

from parsing.parser import Node
import constructs.elements


def process_tree(tree):
    root: Node = tree.root

    def process_branch(branch):

        children: list = branch.children

        children_generator = (child for child in children)

        current_child = next(children_generator, None)
