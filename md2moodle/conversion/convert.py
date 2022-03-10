# md2moodle imports
from md2moodle.compiling.compiler import compile
from md2moodle.compiling.processor import process_tree
from md2moodle.constructs import Prefix_inline_element, build_elements_from_rules
from md2moodle.parsing import parse, Scanner


class Converter:
    def __init__(self, path):
        self.elements = build_elements_from_rules(path)
        self.scanner = Scanner(self.elements)
        self.prefix_elements = [
            element
            for element in self.elements
            if isinstance(element, Prefix_inline_element)
        ]

    def convert_text(self, text):
        self.scanner.pre_scan(text)
        output = self.scanner.scan(text)
        tree = parse(output)
        processed_tree = process_tree(tree)
        compiled_output = compile(processed_tree)
        return compiled_output
