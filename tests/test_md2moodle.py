import json
from collections import namedtuple

import pytest

# md2moodle imports
from md2moodle.compiling.compiler import compile
from md2moodle.compiling.processor import process_tree
from md2moodle.constructs.construct_builder import build_elements_from_rules
from md2moodle.conversion.convert import Converter
from md2moodle.debug import p
from md2moodle.parsing import Scanner, parse


@pytest.fixture
def default_rule(tmp_path):
    f = tmp_path / "rules.json"
    f.write_text(
        json.dumps(
            {
                "rules": [
                    {
                        "name": "spoiler",
                        "element_type": "default",
                        "tokens": {
                            "start_tag": "\\[SPOILER\\]",
                            "end_tag": "\\[/SPOILER\\]",
                        },
                        "actions": {
                            "process_children": "convert_to_html",
                            "add_prefix": "<details>\n<summary>Spoiler</summary>\n",
                            "add_suffix": "</details>",
                        },
                    }
                ]
            }
        )
    )
    return f


@pytest.fixture
def standalone_prefix_rule(tmp_path):
    f = tmp_path / "rules.json"
    f.write_text(
        json.dumps(
            {
                "rules": [
                    {
                        "name": "category_tag",
                        "element_type": "standalone_prefix",
                        "tokens": {"prefix": "(@#)(\\S+)"},
                        "actions": {
                            "add_prefix": '<div><span class="badge" style="font-size:1.2em">',
                            "add_suffix": "</span></div>",
                        },
                    }
                ]
            }
        )
    )
    return f


@pytest.fixture
def prefix_delete_rule(tmp_path):
    f = tmp_path / "rules.json"
    f.write_text(
        json.dumps(
            {
                "rules": [
                    {
                        "name": "todo item",
                        "element_type": "standalone_prefix",
                        "tokens": {"prefix": "(^TODO)(.+)"},
                        "actions": {"process_children": "delete"},
                    },
                ]
            }
        )
    )
    return f


MarkdownHtmlFixture = namedtuple("MarkdownHtmlFixture", ["markdown", "html"])


@pytest.fixture
def simple_spoiler_text():
    return MarkdownHtmlFixture(
        """
[SPOILER]
# Lorem ipsum
In ad nulla commodo mollit eiusmod.
[/SPOILER]
""".strip(),
        """
<details>
<summary>Spoiler</summary>
<h1>Lorem ipsum</h1>

<p>In ad nulla commodo mollit eiusmod.</p>
</details>
""".strip(),
    )


@pytest.fixture
def nested_spoiler_text():
    return MarkdownHtmlFixture(
        """
[SPOILER]
# Lorem ipsum
In ad nulla commodo mollit eiusmod.
[SPOILER]
Irure quis proident sint velit ullamco ea id qui non officia ex nostrud officia.
[/SPOILER]
[/SPOILER]
""".strip(),
        """
<details>
<summary>Spoiler</summary>
<h1>Lorem ipsum</h1>

<p>In ad nulla commodo mollit eiusmod.</p>
<details>
<summary>Spoiler</summary>
<p>Irure quis proident sint velit ullamco ea id qui non officia ex nostrud officia.</p>
</details><p></p>
</details>
""".strip(),
    )


@pytest.fixture
def triple_nested_spoiler_text():
    return MarkdownHtmlFixture(
        """
[SPOILER]
# Lorem ipsum
In ad nulla commodo mollit eiusmod.
[SPOILER]
Irure quis proident sint velit ullamco ea id qui non officia ex nostrud officia.
[SPOILER]
Consectetur occaecat adipisicing adipisicing officia irure.
[/SPOILER]
[/SPOILER]
[/SPOILER]
""".strip(),
        """
<details>
<summary>Spoiler</summary>
<h1>Lorem ipsum</h1>

<p>In ad nulla commodo mollit eiusmod.</p>
<details>
<summary>Spoiler</summary>
<p>Irure quis proident sint velit ullamco ea id qui non officia ex nostrud officia.</p>
<details>
<summary>Spoiler</summary>
<p>Consectetur occaecat adipisicing adipisicing officia irure.</p>
</details><p></p>
</details><p></p>
</details>
""".strip(),
    )


@pytest.fixture
def standalone_prefix_text():
    return MarkdownHtmlFixture(
        """
@#module-project
""".strip(),
        """
<div><span class="badge" style="font-size:1.2em">module-project</span></div>
""".strip(),
    )


# @pytest.fixture
# def default_construct(default_rule):
#     return build_elements_from_rules(default_rule)

# @pytest.fixture
# def standalone_prefix_construct(standalone_prefix_rule):
#     return build_elements_from_rules(standalone_prefix_rule)

# @pytest.fixture
# def prefix_delete_construct(prefix_delete_rule):
#     return build_elements_from_rules(prefix_delete_rule)


def test_constructs_built(default_rule, standalone_prefix_rule, prefix_delete_rule):
    build_elements_from_rules(default_rule)
    build_elements_from_rules(standalone_prefix_rule)
    build_elements_from_rules(prefix_delete_rule)


def test_scanner_built(default_rule, standalone_prefix_rule, prefix_delete_rule):
    Scanner(build_elements_from_rules(default_rule))
    Scanner(build_elements_from_rules(standalone_prefix_rule))
    Scanner(build_elements_from_rules(prefix_delete_rule))


def test_pre_scan(default_rule, standalone_prefix_rule, prefix_delete_rule):
    Scanner(build_elements_from_rules(default_rule)).pre_scan("Hello, World")
    Scanner(build_elements_from_rules(standalone_prefix_rule)).pre_scan("Hello, World")
    Scanner(build_elements_from_rules(prefix_delete_rule)).pre_scan("Hello, World")


def test_simple_spoiler(default_rule, simple_spoiler_text):
    assert (
        Converter(default_rule).convert_text(simple_spoiler_text.markdown)
        == simple_spoiler_text.html
    )


def test_nested_spoiler(default_rule, nested_spoiler_text):
    assert (
        Converter(default_rule).convert_text(nested_spoiler_text.markdown)
        == nested_spoiler_text.html
    )


def test_triple_nested_spoiler(default_rule, triple_nested_spoiler_text):
    assert (
        Converter(default_rule).convert_text(triple_nested_spoiler_text.markdown)
        == triple_nested_spoiler_text.html
    )


def test_standalone_prefix(standalone_prefix_rule, standalone_prefix_text):
    assert (
        Converter(standalone_prefix_rule).convert_text(standalone_prefix_text.markdown)
        == standalone_prefix_text.html
    )
