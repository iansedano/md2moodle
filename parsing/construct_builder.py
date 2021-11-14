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

    def build(self):
        if self.built == False:
            for rule in self.rules:
                print(rule)
                # DEFAULT ELEMENT
                if rule["element_type"] == "default":
                    tokens = map(lambda token: Token(
                        token["name"], token["pattern"]), rule["tokens"])
                    actions = map(
                        lambda action: Action(
                            Action_type[action.type], **action)
                    , tokens)
                    element = Default_element(rule["name"], *tokens)
                    
                # STANDALONE PREFIX
                elif rule.element_type == "standalone_prefix":
                    token = Token(rule.tokens[0].type, rule.tokens[0].pattern)
                    element = Inline_element(rule.name, token)
                self.constructs.append(element)
            self.built = True
        return self.constructs
