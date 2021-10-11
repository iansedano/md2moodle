"""
Building tree to represent text and spoilers
Root is doc root, and then it will have a series of children
Children will either be a line of text,
or a new node with it's own children.
If it is a new node, that node represents a spoiler.

Once the first pass is complete, it will concatenate all adjacent lines
then convert the spoiler nodes to text wrapped with the summary html tags
"""

import pathlib
import re

import markdown2

start_tag = re.compile(r"\[SPOILER\]")
end_tag = re.compile(r"\[\/SPOILER\]")

def to_md(text):
	return markdown2.markdown(text, extras=["fenced-code-blocks"])

def convert_spoilers_to_html(lines):
	line_gen = (line for line in lines)
	
	def convert_spoilers_to_html_helper(line_gen):
		line = next(line_gen, None)
		
		output = []
		current = []
		
		while line:
			
			if start_tag.match(line):
				if line.strip() != "[SPOILER]":
					raise Exception(line, " seems to have something wrong with it", line.strip())
					
				output.append(''.join(current))
				current = []
				output.append('<details>\n<summary>Spoiler</summary>')
				output.append(convert_spoilers_to_html_helper(line_gen))
				output.append("</summary>")
				
			elif end_tag.match(line):
				if line.strip() != "[/SPOILER]":
					raise Exception(line, " seems to have something wrong with it")
				
				output.append(
					to_md(''.join(current))
				)
				
				return ''.join(output)
				
			else:
				current.append(line)
				
			line = next(line_gen, None)
		
		print(output)
		return ''.join(output)
	
	return convert_spoilers_to_html_helper(line_gen)

'''
<details>
<summary>Spoiler</summary>
<p>hidden stuff</p>
</details>
'''

	

def process_spoilers(p):
	path = pathlib.Path(p)
	
	with open(path, mode='r+') as f:
		html = convert_spoilers_to_html(f.readlines())
		print(html)

process_spoilers(R"C:\Dev\0 Git sync\react-course\00-js2-react\Course-01-Advanced JS\003-Connect 4\002-Basic State\006-modularizing.md")