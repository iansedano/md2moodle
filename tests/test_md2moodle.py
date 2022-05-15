import pytest

import json

# md2moodle imports
from md2moodle.compiling.compiler import compile
from md2moodle.compiling.processor import process_tree
from md2moodle.constructs.construct_builder import build_elements_from_rules
from md2moodle.conversion.convert import Converter
from md2moodle.debug import p
from md2moodle.parsing import parse, Scanner


@pytest.fixture
def default_rule():
    return json.dumps(
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
                        "add_prefix": "<details>\n<summary>Spoiler</summary>",
                        "add_suffix": "</details>",
                    },
                }
            ]
        }
    )


@pytest.fixture
def standalone_prefix_rule():
    return json.dumps(
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


@pytest.fixture
def prefix_delete_rule():
    return json.dumps(
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


@pytest.fixture
def raise_exception():
    5 / 0


@pytest.mark.skip
def test_constructs_built(default_rule, standalone_prefix_rule, prefix_delete_rule):
    build_elements_from_rules(default_rule)
    build_elements_from_rules(standalone_prefix_rule)
    build_elements_from_rules(prefix_delete_rule)


def test_scanner_initializes():
    ...
