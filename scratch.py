from constructs.construct_builder import Construct_builder
from parsing.scanner import Scanner
from parsing.parser import Parser

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
print("CONSTRUCTS BUILT")
scanner = Scanner(constructs)
print("SCANNER BUILT")

scanner.pre_scan(text)
print("TEXT SCANNED")
output = scanner.scan(text)

parser = Parser()
print("PARSER BUILT")

tree = parser.parse(output)
print("TREE BUILT")

print("tree", tree)
