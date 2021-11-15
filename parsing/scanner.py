from parsing.constructs import Element


class Scanner:
    def __init__(self, constructs: list[Element]):
        self.constructs = constructs
        self.patterns = []
        for construct in constructs:
            for token in construct.get_tokens():
                self.patterns.append(token.pattern)
        self.errors = []

    def check(self, line):
        for pattern in self.patterns:
            matches = pattern.findall(line)
            if len(matches) > 1:
                self.errors.append(
                    "ERROR '" + line + "'. Only one tag per line")
            elif len(matches) == 1:
                if not pattern.match(line):
                    self.errors.append(
                        "ERROR '" + line + "'. Tag must be only thing on line")

    def match(self, line):
        for construct in self.constructs:
            for token in construct.get_tokens():
                if token.pattern.match(line):
                    return token

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
            token = self.match(line)
            if token:
                output.append(token)
            else:
                output.append(line)
        return output
