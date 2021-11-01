from dataclasses import dataclass
from enum import Enum, auto
import re

from pprint import pp

class Token_enum(Enum):
	OPEN_TAG = auto()
	CLOSE_TAG = auto()
	STANDALONE = auto()

class Token:
	def __init__(self, name: str, token_type: Token_enum, regex: str):
		self.name, self.token_type = name, token_type
		self.regex = re.compile(regex)
		
	def __repr__(self):
		return (f"{self.name}, {self.token_type}, {self.regex}")
	
	def __eq__(self, other):
		return (
			self.name == other.name and
			self.token_type == other.token_type			
		)
		
	def match(self, string, flags=0):
		return re.match(self.regex, string, flags)





