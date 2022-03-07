# md2moodle imports
from md2moodle.compiling.compiler import compile
from md2moodle.compiling.processor import process_tree
from md2moodle.constructs.construct_builder import build_elements_from_rules
from md2moodle.constructs.elements import Prefix_inline_element
from md2moodle.parsing.parser import Parser
from md2moodle.parsing.scanner import Scanner


class Converter:
    def __init__(self, path):
        self.constructs = build_elements_from_rules(path)
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
        tree = self.parser.parse(output)
        processed_tree = process_tree(tree)
        compiled_output = compile(processed_tree)
        return compiled_output
