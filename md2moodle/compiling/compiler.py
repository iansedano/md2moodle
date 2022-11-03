"""Will compile the processed tree into final output
"""


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
