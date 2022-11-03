"""Scanner
First pass of the text, identifying the tokens defined in the constructs.
e.g.:

[SPOILER]  - TOKEN
This is a spoiler
[/SPOILER]  - TOKEN
"""

# md2moodle imports
from md2moodle.constructs import Element
from md2moodle.parsing.tokens import Token_type_enum


class Scanner:
    """Scans text and produces list of tokens based on a list of constructs available"""

    def __init__(self, constructs: list[Element]):
        self.constructs = constructs
        self.patterns = []
        for construct in constructs:
            for token in construct.get_tokens():
                self.patterns.append(token.pattern)
        self.errors: list = []

    def check(self, line):
        for pattern in self.patterns:
            matches = pattern.findall(line)
            if len(matches) > 1:
                self.errors.append("ERROR '" + line + "'. Only one tag per line")
            elif len(matches) == 1:
                if not pattern.match(line):
                    self.errors.append(
                        "ERROR '" + line + "'. Tag must be only thing on line"
                    )

    def match(self, line):
        for construct in self.constructs:
            for token in construct.get_tokens():
                match = token.pattern.match(line)
                if match:
                    return match, token
        return None, None

    def pre_scan(self, text):
        lines = text.split("\n")
        for line in lines:
            self.check(line)
        if self.errors:
            raise SyntaxError("\n" + "\n".join(self.errors))

    def scan(self, text):
        output = []
        lines = text.split("\n")
        for line in lines:
            match, token = self.match(line)
            if token:
                # This is opt out of inline elements because they are matched and replaced during processing
                if token.token_type == Token_type_enum.PREFIX:
                    output.append(token)
                    output.append(match[2])
                else:
                    output.append(token)
            else:
                output.append(line)
        return output
