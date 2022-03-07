from enum import IntEnum
from md2moodle.parsing.parser import Node

import markdown2
import re

def md_to_html(text):
    
    link_patterns = [
        (re.compile(r'^\[([\w\s\d]+)\]\((https?:\/\/[\w\d./?=#]+)\)$'),r'\1')
    ]
    
    return markdown2.markdown(
        text,
        extras={
            "fenced-code-blocks": None,
            "link-patterns": None,
            "html-classes": {"img": "img-responsive cn-imgage"},
            "target-blank-links": None
        },
        link_patterns=link_patterns
    )

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
