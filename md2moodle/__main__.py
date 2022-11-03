# Standard library imports
import argparse
import contextlib
from pathlib import Path

# md2moodle imports
from md2moodle.conversion.course_export import export_course

DEFAULT_RULES_FILE_NAME = "rules.json"
DEFAULT_FILE_GLOB = "**/*.md"
DEFAULT_OUTPUT_PATH = "moodle-dist"


class ArgsError(Exception):
    pass


def parse_args():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("course_root")
    arg_parser.add_argument("-o", "--output-path", default=DEFAULT_OUTPUT_PATH)
    arg_parser.add_argument("-g", "--glob", default=DEFAULT_FILE_GLOB)
    arg_parser.add_argument("-r", "--rules", default=DEFAULT_RULES_FILE_NAME)

    return arg_parser.parse_args()


def validate(args):
    if not Path(DEFAULT_RULES_FILE_NAME).exists():
        raise ArgsError("No rules file detected at root")


def main():
    try:
        args = parse_args()
        validate(args)
        print(args)
    except ArgsError as e:
        print(f"Error: {e}")
        raise SystemExit from e

    with contextlib.suppress(KeyboardInterrupt):
        export_course(
            Path(args.rules),
            Path(args.course_root),
            args.glob,
            Path(args.output_path),
        )
