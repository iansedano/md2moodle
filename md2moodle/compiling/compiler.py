"""Will compile the processed tree into final output
"""

# Standard library imports
import re

# md2moodle imports
import md2moodle.constructs.action
import md2moodle.constructs.elements


def compile(tree):
    output = []

    def helper(node):
        for child in node.children:
            if isinstance(child, str):
                output.append(child)
            else:
                helper(child)

    helper(tree)

    output = "".join(output)

    return output
