from tokens import Token, Token_enum
import abc

tokens = [
	Token("SPOILER"		, Token_enum.OPEN_TAG	, r"\[SPOILER\]"	),
	Token("SPOILER"		, Token_enum.CLOSE_TAG	, r"\[\/SPOILER\]"	),
	Token("NOTE"		, Token_enum.OPEN_TAG	, r"\[NOTE\]"		),
	Token("NOTE"		, Token_enum.CLOSE_TAG	, r"\[\/NOTE\]"		),
	Token("ALERT"		, Token_enum.OPEN_TAG	, r"\[ALERT\]"		),
	Token("ALERT"		, Token_enum.CLOSE_TAG	, r"\[\/ALERT\]"	),
	Token("TAG"			, Token_enum.STANDALONE	, r"@#\w+"			)
]

class Element(metaclass=abc.ABCMeta):
	
	@abc.abstractmethod
	def get_tokens(self) -> list[Token]:
		raise NotImplementedError
		
	@abc.abstractmethod
	def convert(self) -> str:
		raise NotImplementedError

# TODO init with children??
class Spoiler(Element):
	def __init__(self):
		self.open_tag = Token("SPOILER"	, Token_enum.OPEN_TAG, r"\[SPOILER\]")
	
	def get_tokens(self):
		return [self.open_tag, self.close_tag]
		
	def convert(self):
		
		
class Replacement(Element):
	def __init__(self, token: Token, replacement: str, content: str):
		self.token = token
		self.replacement = replacement
		
	def convert(self):
		