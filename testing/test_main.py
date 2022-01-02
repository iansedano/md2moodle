from constructs.construct_builder import Construct_builder
from constructs.elements import Prefix_inline_element
from parsing.scanner import Scanner
from parsing.parser import Parser
from compiling.processor import process_tree
from compiling.compiler import compile

from debug import p

SAMPLE_INPUT_A = """
@#module-project
hello these are words
and does the newline
[SPOILER]
### Try this header
actually get on it's own thing
sdjklsd
[/SPOILER]
sdasd
[ALERT]
WATCH OUT!
[/ALERT]
"""


def test_parser():
    construct_builder = Construct_builder("rules.json")
    constructs = construct_builder.build()
    p(constructs)
    print("CONSTRUCTS BUILT\n\n")
    scanner = Scanner(constructs)
    p(scanner)
    print("SCANNER BUILT\n\n")

    scanner.pre_scan(SAMPLE_INPUT_A)
    print("TEXT PRE SCANNED\n\n")
    output = scanner.scan(SAMPLE_INPUT_A)
    p(output)
    print("TEXT SCANNED\n\n")

    parser = Parser()
    print("PARSER BUILT\n\n")

    tree = parser.parse(output)
    p(tree)
    print("TREE BUILT\n\n")

    processed_tree = process_tree(tree)
    p(processed_tree)
    print("TREE PROCESSED\n\n")

    prefix_constructs = [
        construct
        for construct in constructs
        if isinstance(construct, Prefix_inline_element)
    ]

    compiled_output = compile(processed_tree, prefix_constructs)
    print(compiled_output)


#     assert (
#         compile(processed_tree)
#         == """
# hello these are words
# and does the newline<details>
# <summary>Spoiler</summary><h3>Try this header</h3>

# <p>actually get on it's own thing
# sdjklsd</p>
# </details>sdasd<div class="alert alert-warning" role="alert"><p>WATCH OUT!</p>
# </div>"""
#     )


test_parser()
