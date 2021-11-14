from parsing.tokens import Token
from parsing.constructs import Default_element, Inline_element
from action import Action, Action_type

from rule_reader.file_reader import File_reader


class Construct_builder:
    def __init__(self, path: str):
        self.constructs = []
        rule_reader = File_reader(path)
        self.rules = rule_reader.get_rules()
        self.built = False

    def _build_token(self, token_dict):
        return Token(token_dict["type"], token_dict["pattern"])

    def _build_action(self, action_dict):
        return Action(Action_type[action_dict["type"]], **action_dict)

    def build(self):
        if self.built == False:
            for rule in self.rules:

                # DEFAULT ELEMENT
                if rule["element_type"] == "default":
                    tokens = map(self._build_token, rule["tokens"])
                    actions = map(self._build_action, rule["actions"])
                    element = Default_element(
                        rule["name"], *tokens, actions=actions)

                # STANDALONE PREFIX
                elif rule["element_type"] == "standalone_prefix":
                    if (len(rule["tokens"]) > 1):
                        raise Exception(
                            "standalone elements should have only one token")
                    token = Token(rule["tokens"][0]["type"],
                                  rule["tokens"][0]["pattern"])
                    actions = map(self._build_action, rule["actions"])
                    element = Inline_element(
                        rule["name"], token, actions=actions)

                self.constructs.append(element)
            self.built = True
        return self.constructs
