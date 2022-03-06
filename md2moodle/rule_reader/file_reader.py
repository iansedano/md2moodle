# Standard library imports
from json import loads as load_json
from pathlib import Path


class File_reader:
    def __init__(self, path: str):
        _path: Path = Path(path)
        self.json = load_json(_path.read_text())

    def get_rules(self):
        return self.json["rules"]
