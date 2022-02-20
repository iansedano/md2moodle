import argparse
from pathlib import Path
from conversion.course_export import export_course

arg_parser = argparse.ArgumentParser(
    description="Exports markdown files to Moodle compatible format\n\n"
    "Sample usage:\n"
    R"python export.py rules.json source **/*.md dest"
    "Will replicate folder structure at dest"
    R"result if source\course -> dest\course"
)

arg_parser.add_argument("rules")
arg_parser.add_argument("course_root")
arg_parser.add_argument("glob")
arg_parser.add_argument("export_dest")


args = arg_parser.parse_args()

export_course(
    Path(args.rules), Path(args.course_root), args.glob, Path(args.export_dest)
)
