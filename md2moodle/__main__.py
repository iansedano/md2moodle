# Standard library imports
import argparse
from pathlib import Path

# md2moodle imports
from md2moodle.conversion.course_export import export_course

arg_parser = argparse.ArgumentParser(
    description="Exports markdown files recursively to Moodle compatible format\n\n"
    "Usage:\n"
    "python -m md2moodle <source> <destination>\n"
    "Example:\n"
    "python -m md2moodle course distribution\n"
    "Will replicate folder structure at destination:\n"
    "source\\course -> distribution\\course"
)

# arg_parser.add_argument("rules")
arg_parser.add_argument("course_root")
# arg_parser.add_argument("glob")
arg_parser.add_argument("export_dest")


args = arg_parser.parse_args()

export_course(
    Path("rules.json"), Path(args.course_root), "**/*.md", Path(args.export_dest)
)
