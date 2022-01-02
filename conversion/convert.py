from constructs.construct_builder import Construct_builder
from constructs.elements import Prefix_inline_element
from parsing.scanner import Scanner
from parsing.parser import Parser
from compiling.processor import process_tree
from compiling.compiler import compile


class Converter:
    def __init__(self, path):
        construct_builder = Construct_builder(path)
        self.constructs = construct_builder.build()
        self.scanner = Scanner(self.constructs)
        self.parser = Parser()
        self.prefix_constructs = [
            construct
            for construct in self.constructs
            if isinstance(construct, Prefix_inline_element)
        ]

    def convert_text(self, text):
        self.scanner.pre_scan(text)
        output = self.scanner.scan(text)
        print("\nSCANNED")
        print(output)
        tree = self.parser.parse(output)
        print("\nTREE")
        print(tree)
        processed_tree = process_tree(tree)
        print("\nPROCESSED TREE")
        print(processed_tree)
        compiled_output = compile(processed_tree)
        return compiled_output
