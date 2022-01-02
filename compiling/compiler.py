"""Will compile the processed tree into final output
"""

import re


def compile(tree, prefix_constructs):
    output = []

    def helper(node):
        for child in node.children:
            if isinstance(child, str):
                output.append(child)
            else:
                helper(child)

    helper(tree)

    output = "".join(output)
    print(output)

    for construct in prefix_constructs:
        print(construct)
        token = construct.get_tokens()[
            0
        ]  # TODO make sure prefix constructs only have one token
        match = token.pattern.search(output)
        while match:
            tag = match[2]
            start = match.start() - 1
            end = match.end()
            output = output[:start] + 
