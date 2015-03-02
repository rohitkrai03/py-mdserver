import re
import os
import markdown


def convert_markdown(doc):
	# open the .md version of doc
	contents = open(os.path.normpath("../docs/" + doc + ".md")).read()

	# convert it to markdown
	html = markdown.markdown(contents)

	# return it to the browser
	return html






def troll_directories(start):
	# troll for all the directories like in find
	results = []
	# Traverse the directory for all the files.
	for root, dirs, files in os.walk(start):
		for fname in files:
			# put the full path into the results
			results.append(os.path.join(root, fname))
	return results


def discover_targets(files):
	results = []
	# get each file
	for source_file in files:
		# strip extension of source file
		base, ext = os.path.splitext(source_file)
		path = base[len(source)+1:]
		target_dir = os.path.dirname(os.path.join(target, path))

		if not os.path.exists(target_dir):
			os.makedirs(target_dir)

		# append .html to the base file name
		target_file = os.path.join(target, path + '.html')
		results.append(source_file, target_file)

	return results

def generate_html(source_file, target_file):
	# open the source file
	contents = open(source_file).read()

	# convert to markdown
	html = markdown.markdown(contents)

	# open output with .html
	with open(target_file, 'w') as f:
		# write html to .html
		f.write(html)


def convert_md_directory(source, target):
	# get all the files in the source
	sources = troll_directories(source)
	targets = discover_targets(sources)

	for source_file, target_file in targets:
		generate_html(source_file, target_file)
