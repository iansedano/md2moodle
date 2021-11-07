from pathlib import Path
from json import loads as load_json

from tokens import Token
from constructs import Default_element, Inline_element
from action import Action, Action_type


class Construct_builder:
    def __init__(self, path):
        self.constructs = []
        path = Path(path)
        json = load_json(path.read_text())
        self.rules = json.rules
        self.built = False

    def build(self):
        if self.build == False:
            for rule in self.rules():
                # DEFAULT ELEMENT
                if rule.element_type == "default":
                    tokens = map(lambda token: Token(
                        token.name, token.pattern), rule.tokens)
                    actions = map(
                        lambda action: Action(
                            Action_type[action.type], **action)
                    )
                    element = Default_element(rule.name, *tokens)
                # STANDALONE PREFIX
                elif rule.element_type == "standalone_prefix":
                    token = Token(rule.tokens[0].type, rule.tokens[0].pattern)
                    element = Inline_element(rule.name, token)
                self.constructs.append(element)
            self.built = True
        return self.constructs
