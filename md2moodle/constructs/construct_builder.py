"""Element Builder - where the information that comes in via JSON gets
translated into classes that will parse and act on the text.

If there is a new element type, or new rule, it needs to be handled here.
"""

# Standard library imports
import json
from pathlib import Path

# md2moodle imports
from md2moodle.constructs.elements import (Default_element, Element,
                                           Prefix_inline_element)
from md2moodle.parsing.tokens import Token, Token_type_enum


def read_rule_file(path_to_rules_file):
    return json.loads(Path(path_to_rules_file).read_text())


def build_elements_from_rules(path_to_rules_file) -> list[Element]:

    elements: list = []
    rules = read_rule_file(Path(path_to_rules_file))["rules"]

    for rule in rules:

        # DEFAULT
        if rule["element_type"] == "default":
            start_tag = Token(
                token_type=Token_type_enum.START_TAG,
                pattern=rule["tokens"]["start_tag"],
            )

            end_tag = Token(
                token_type=Token_type_enum.END_TAG,
                pattern=rule["tokens"]["end_tag"],
            )

            element = Default_element(
                name=rule["name"],
                start_tag=start_tag,
                end_tag=end_tag,
                actions=rule["actions"],
            )

            element.start_tag.add_parent(element)
            element.end_tag.add_parent(element)

        # PREFIX INLINE
        elif rule["element_type"] == "standalone_prefix":
            if len(rule["tokens"]) > 1:
                raise Exception("standalone elements should have only one token")

            prefix = Token(
                token_type=Token_type_enum.PREFIX,
                pattern=rule["tokens"]["prefix"],
            )

            element = Prefix_inline_element(
                name=rule["name"], prefix=prefix, actions=rule["actions"]
            )

            element.prefix.add_parent(element)

        elements.append(element)

    return elements
