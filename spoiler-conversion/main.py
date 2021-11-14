import pathlib
import json

from process_spoilers import process_spoilers

config_path = pathlib.Path("scripts-config.json")

config = json.loads(
	config_path.read_text()
	)
print(config['course-paths'])

course_paths = [ pathlib.Path(p) for p in config['course-paths'] ]

for course_path in course_paths:
	for path in course_path.glob('**/*.md'):
		process_spoilers(path)
		

