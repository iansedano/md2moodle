from constructs.construct_builder import Construct_builder
from constructs.elements import Prefix_inline_element
from parsing.scanner import Scanner
from parsing.parser import Parser
from compiling.processor import process_tree
from compiling.compiler import compile

from conversion.convert import Converter

from pathlib import Path

from debug import p

SAMPLE_INPUT_A = """
@#module-project
hello these are words
and does the newline
[SPOILER]
### Try this header
actually get on it's own thing
sdjklsd
[/SPOILER]
sdasd
[ALERT]
WATCH OUT!
[/ALERT]
"""

SAMPLE_INPUT_A_CONVERTED = """<span class="badge badge-pill badge-primary" style="font-size:1.2em; background-color:#fbb03b; color:black"><p>module-project</p>
</span>hello these are words
and does the newline<details>
<summary>Spoiler</summary><h3>Try this header</h3>

<p>actually get on it's own thing
sdjklsd</p>
</details>sdasd<div class="alert alert-warning" role="alert"><p>WATCH OUT!</p>
</div>"""


def test_simple():
    construct_builder = Construct_builder("rules.json")
    constructs = construct_builder.build()
    p(constructs)
    print("CONSTRUCTS BUILT\n\n")
    scanner = Scanner(constructs)
    p(scanner)
    print("SCANNER BUILT\n\n")

    scanner.pre_scan(SAMPLE_INPUT_A)
    print("TEXT PRE SCANNED\n\n")
    output = scanner.scan(SAMPLE_INPUT_A)
    p(output)
    print("TEXT SCANNED\n\n")

    parser = Parser()
    print("PARSER BUILT\n\n")

    tree = parser.parse(output)
    p(tree)
    print("TREE BUILT\n\n")

    processed_tree = process_tree(tree)
    p(processed_tree)
    print("TREE PROCESSED\n\n")

    compiled_output = compile(processed_tree)

    assert compiled_output == SAMPLE_INPUT_A_CONVERTED


test_simple()


def test_nested():
    text = Path("testing/nested.md").read_text()

    construct_builder = Construct_builder("rules.json")
    constructs = construct_builder.build()
    p(constructs)
    print("CONSTRUCTS BUILT\n\n")
    scanner = Scanner(constructs)
    p(scanner)
    print("SCANNER BUILT\n\n")

    scanner.pre_scan(text)
    print("TEXT PRE SCANNED\n\n")
    output = scanner.scan(text)
    p(output)
    print("TEXT SCANNED\n\n")

    parser = Parser()
    print("PARSER BUILT\n\n")

    tree = parser.parse(output)
    p(tree)
    print("TREE BUILT\n\n")

    processed_tree = process_tree(tree)
    p(processed_tree)
    print("TREE PROCESSED\n\n")

    compiled_output = compile(processed_tree)
    assert (
        compiled_output
        == """<details>
<summary>Spoiler</summary><p>Here is a hint</p>
<details>
<summary>Spoiler</summary><p>here is the code</p>

<pre><code>&lt;Terminal&gt;&lt;/Terminal&gt;
</code></pre>
</details><p></p>
</details>"""
    )


test_nested()


def test_files():
    converter = Converter("rules.json")
    converter.convert_text(SAMPLE_INPUT_A) == SAMPLE_INPUT_A_CONVERTED

    test_files = ["01.md", "002-landing page.md", "003-Updating the board.md"]

    for path in test_files:
        print("\n\nNEW FILE\n\n")
        full_path = "testing/" + path
        result_path = full_path[:-3] + "_result.md"
        print(result_path)
        text = Path(full_path).read_text()
        converted_text = converter.convert_text(text)
        print(converted_text)
        assert converted_text == Path(result_path).read_text()


test_files()
