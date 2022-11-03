"""
The regex matches all Markdown links of the form following form:
    [Example](http://www.example.com)
and replaces them with new-tab HTML links, e.g.:
    <a href="http://www.example.com" target="_blank">Example</a>
    
Also image links in following form:
    ![Example](http://www.example.com/image.jpg)
and replaces them with HTML <img> elements, e.g.:
    '<img src="http://www.example.com/image.jpg" alt="Example" class="cn_image img-responsive">
"""

# Standard library imports
import argparse
import re
from pathlib import Path

FILE_COUNT, REPLACEMENT_COUNT = 0, 0
HYPERLINK_PATTERN = re.compile(r"(?<!!)\[(.+?)\]\((.+?)\)")
IMAGE_PATTERN = re.compile(r"\!\[([^\]]+)\]\(([^\)]+)\)")


def parse_args():
    parser = argparse.ArgumentParser(prog="Link Replacer")
    parser.add_argument("path", default=".")
    return parser.parse_args()


def update_hyperlinks(match):
    """Creates a HTML link that opens in a new tab from an appropriate re.match() object."""
    global REPLACEMENT_COUNT
    text = match.group(1)
    url = match.group(2)
    REPLACEMENT_COUNT += 1
    return f'<a href="{url}" target="_blank">{text}</a>'


def update_image_links(match):
    global REPLACEMENT_COUNT
    text = match.group(1)
    url = match.group(2)
    REPLACEMENT_COUNT += 1
    return f'<img src="{url}" alt="{text}" class="cn_image img-responsive">'


def replace_content(content):
    content = re.sub(HYPERLINK_PATTERN, update_hyperlinks, content)
    content = re.sub(IMAGE_PATTERN, update_image_links, content)
    return content


def replace_md_links(directory):
    """Replaces all Markdown-style links with HTML new-tab links recursively in a folder structure."""
    global FILE_COUNT
    print(f"Replacing links in {directory.name}")
    for file in directory.rglob("*.md"):
        if file.name != "README.md":
            print(f"Starting on file {file.name}")
            FILE_COUNT += 1

            with open(file.absolute(), "r+", encoding="utf8") as f:
                content = f.read()
                f.seek(0)
                f.truncate()
                f.write(replace_content(content))


def main():
    args = parse_args()
    replace_md_links(Path(args["path"]))
    print(
        f"Done. Replaced {REPLACEMENT_COUNT} links across {FILE_COUNT} files."
    )


if __name__ == "__main__":
    main()
