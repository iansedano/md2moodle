from scanner import Scanner
from parser import Parser
from constructs import constructs
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
