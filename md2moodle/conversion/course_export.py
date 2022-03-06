from pathlib import Path
from shutil import rmtree
from md2moodle.conversion.convert import Converter


def export_course(rules: Path, course_root: Path, glob: str, output: Path):

    converter = Converter(rules)
    output = Path(output.absolute())
    if output.exists():
        rmtree(output)

    Path.mkdir(output)

    files = course_root.absolute().glob(glob)

    root_len = len(course_root.absolute().parts)

    for file in files:
        try:
            text = converter.convert_text(file.read_text())
            parts = file.parts[root_len:]
            new_path = Path(output, *parts)
            folder_of_new_path = Path(*new_path.parts[:-1])
            if not folder_of_new_path.exists():
                Path.mkdir(folder_of_new_path, parents=True)
            new_path.write_text(text)
        except Exception as e:
            print(f"Failed at {file.absolute()}\n {e}")
