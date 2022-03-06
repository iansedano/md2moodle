from tokens import tokens, Token_type_enum

from pprint import pp


def convert_spoilers_to_html(lines):
    line_gen = (line for line in lines)

    def convert_spoilers_to_html_helper(line_gen):
        line = next(line_gen, None)
        output = []
        current = []

        while line:
            if start_tag.match(line):
                if line.strip() != "[SPOILER]":
                    raise Exception(
                        line, "seems to have something wrong with it")

                output.append(''.join(current))
                current = []
                output.append('<details>\n<summary>Spoiler</summary>')
                output.append(convert_spoilers_to_html_helper(line_gen))
                output.append("</summary>")

            elif end_tag.match(line):
                if line.strip() != "[/SPOILER]":
                    raise Exception(
                        line, "seems to have something wrong with it")
                output.append(to_md(''.join(current)))
                return ''.join(output)

            else:
                current.append(line)
            line = next(line_gen, None)
        output.append(''.join(current))
        return ''.join(output)

    return convert_spoilers_to_html_helper(line_gen)


def process_spoilers(p):
    path = pathlib.Path(p)

    with open(path, mode='r+') as f:
        try:
            converted_text = convert_spoilers_to_html(f.readlines())
            f.seek(0)
            f.write(converted_text)
            f.truncate()
        except:
            print("something wrong with file", path)


process_spoilers(
    R"C:\Dev\0 Git sync\react-course\00-js2-react\Course-01-Advanced JS\003-Connect 4\003-Display\002-Your own library.md")
