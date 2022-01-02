import re


pattern = "(@#)(\\w+)"

pattern = re.compile(pattern, re.MULTILINE)
print(pattern)


ex = """
@#module-project
"""

print(pattern.findall(ex))
