from scanner import Scanner
from constructs import constructs
text = """
hello these are words
and does the newline
[SPOILER][SPOILER]
actually get [SPOILER] on it's own thing
"""

myscanner = Scanner(constructs)

myscanner.scan(text)
print(myscanner.errors)
