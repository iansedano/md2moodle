# Standard library imports
from enum import IntEnum

# Third party imports
import markdown2

# md2moodle imports
from md2moodle.parsing import Node


def md_to_html(text):
	return markdown2.markdown(text, extras=["fenced-code-blocks"])

class Action_type(IntEnum):
    process_children = 1
    add_prefix = 2
    add_suffix = 3


class Action:
    def __init__(self, type: Action_type, payload: str):
        self.type = type
        self.payload = payload
        self.execute = self.define_action()

    def define_action(self):
        match self:
            case Action(type=Action_type.add_prefix):
                return self.add_prefix
            case Action(type=Action_type.add_suffix):
                return self.add_suffix
            case Action(type=Action_type.process_children, payload="convert_to_html"):
                return self.process_children_convert_to_html
            case Action(type=Action_type.process_children, payload="delete"):
                return self.delete_children
        
    
    def add_suffix(self, node: Node):
        node.children.append(self.payload)

    def add_prefix(self, node: Node):
        node.children.insert(0, self.payload)

    def process_children_convert_to_html(self, node: Node):
        
        new_children = []
        
        for child in node.children:
            
            if isinstance(child, str):
                new_children.append(md_to_html(child))
            else:
                new_children.append(child)
        node.children = new_children
    
    def delete_children(self, node: Node):
        node.children = []
