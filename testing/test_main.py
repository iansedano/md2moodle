from constructs.construct_builder import Construct_builder
from parsing.scanner import Scanner
from parsing.parser import Parser
from compiling.processor import process_tree

SAMPLE_INPUT_A = """
hello these are words
and does the newline
[SPOILER]
actually get on it's own thing
[/SPOILER]
sdasd
[ALERT]
WATCH OUT!
[/ALERT]
"""


def test_parser():
    construct_builder = Construct_builder("rules.json")
    constructs = construct_builder.build()
    print("CONSTRUCTS BUILT", constructs)
    scanner = Scanner(constructs)
    print("SCANNER BUILT", scanner)

    scanner.pre_scan(SAMPLE_INPUT_A)
    print("TEXT SCANNED")
    output = scanner.scan(SAMPLE_INPUT_A)
    print(output)
    parser = Parser()
    print("PARSER BUILT")

    tree = parser.parse(output)
    print("TREE BUILT")

    print("tree", tree)
    print("STARTING PROCESSING")
    processed_tree = process_tree(tree)


test_parser()
