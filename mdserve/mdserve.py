
from flask import Flask
import markdown
import utils
import os
from flask import render_template
from flask import request
from flask import abort, redirect, url_for

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	# convert the markdown
	html = utils.convert_markdown("index")
	# Render the contents with templates
	return render_template("layout.html", body=html, doc="index")
	# return to browser
    # return utils.convert_markdown('index')


# if they go to .html, serve that .md file
# /stuff/index.html
# /foo.html
@app.route('/<doc>.html')
def mdfile(doc):
	html =  utils.convert_markdown(doc)

	return render_template("layout.html", body=html,  doc=doc)

# if they go to any other directory, serve that index.html
# /stuff/
# /hello/there/you
@app.route('/<subdir>/')
def sub_directory(subdir):
	# get the index.md file for subdir
	docs =  os.path.join(subdir, "index")

	html =  utils.convert_markdown(docs)
	return render_template("layout.html", body=html, doc='index')


@app.route("/edit/<doc>.html", methods=['POST', 'GET'])
def edit(doc):
	# if the are posting a change
	if request.method == 'POST':
		contents = request.form["contents"]

		# write the new contents to file
		with open(os.path.normpath("../docs/" + doc + ".md"), 'w') as f:
			f.write(contents)
		# redirect to new file
		return redirect(doc + '.html')
	else:
		# if they are getting the file
		# load the raw md file
		contents = open(os.path.normpath("../docs/" + doc + ".md")).read()
		# give the edit template
		return render_template("edit.html", doc=doc, contents=contents)

	



if __name__ == "__main__":
    app.run()


