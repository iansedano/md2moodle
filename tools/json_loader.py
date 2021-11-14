from pathlib import Path
from json import loads as load_json

class File_reader:
	def __init__(self, path: str):
		path : Path = Path(path)
		self.json = load_json(path.read_text())
		
	def get_rules(self):
		return self.json["rules"]