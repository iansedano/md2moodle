import argparse
from pathlib import Path
from conversion.course_export import export_course

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("rules")
arg_parser.add_argument("course_root")
arg_parser.add_argument("glob")
arg_parser.add_argument("export_dest")


args = arg_parser.parse_args()

export_course(
    Path(args.rules),
    Path(args.course_root),
    args.glob,
    Path(args.export_dest)
)
