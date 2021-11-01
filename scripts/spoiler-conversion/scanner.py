

class Scanner:
    def __init__(self, constructs):
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

    def scan(self, text):
        lines = text.split("\n")
        for line in lines:
            self.check(line)
        if self.errors:
            raise SyntaxError("\n" + "\n".join(self.errors))
