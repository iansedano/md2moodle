"""
Building tree to represent text and spoilers
Root is doc root, and then it will have a series of children
Children will either be a line of text,
or a new node with it's own children.
If it is a new node, that node represents a spoiler.
"""

import pathlib
import re

import markdown2

class node():
	def __init__(self):
		self.children = []


def build_spoiler_tree(lines):
	root = node()
	
	start_tag = re.compile(r"\[SPOILER\]")
	end_tag = re.compile(r"\[\/SPOILER\]")
	
	line_gen = (line for line in lines)
	line = next(line_gen, None)
	
	current_node = root
	
	while line:
		
		# if start_tag.match(line):
		# 	new_node = node()
		# 	current_
		
		
			
		line = next(line_gen, None)
	

def convert_tree_to_html(root):
	'''
	<details>
	<summary>spoiler</summary>
	<p>hidden stuff</p>
	</details>
	'''
	return
	

def process_spoilers(p):
	path = pathlib.Path(p)
	print(markdown2.markdown(path.read_text(), extras=["fenced-code-blocks"]))
	
	# with open(path, mode='r+') as f:
	# 	spoiler_tree = build_spoiler_tree(f.readlines())

process_spoilers(R"C:\Dev\0 Git sync\react-course\00-js2-react\Course-01-Advanced JS\003-Connect 4\002-Basic State\006-modularizing.md")