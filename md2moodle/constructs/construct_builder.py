"""Construct Builder - where the information that comes in via JSON gets
translated into classes that will parse and act on the text.

If there is a new construct type, or new rule, this is where it should go.
"""

# Standard library imports
from json import loads as load_json
from pathlib import Path

# md2moodle imports
from md2moodle.constructs.elements import Default_element, Prefix_inline_element
from md2moodle.parsing.tokens import Token, Token_type_enum


def build_elements_from_rules(path_to_rules_file):

    elements: list = []
    json = load_json(Path(path_to_rules_file).read_text())
    rules = json["rules"]

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
