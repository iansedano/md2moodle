
# from parsing.parser import Parser
from parsing.construct_builder import Construct_builder
from parsing.scanner import Scanner

text = """
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

construct_builder = Construct_builder("rules.json")
constructs = construct_builder.build()

scanner = Scanner(constructs)

for c in constructs:
    for a in c.actions:
        print(a.payload)


# scanner = Scanner(constructs)

# scanner.pre_scan(text)

# output = scanner.scan(text)
# print(output)
# parser = Parser()
# tree = parser.parse(output)

# print("tree", tree)


class test:
    def __init__(self):
        self.a = self.get_num()

    def get_num(self):
        return 10


print(test().a)
