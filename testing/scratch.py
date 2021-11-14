from parsing.scanner import Scanner
from parsing.parser import Parser
import parsing.constructs as constructs

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

scanner = Scanner(constructs)

scanner.pre_scan(text)

output = scanner.scan(text)
print(output)
parser = Parser()
tree = parser.parse(output)

print("tree", tree)
