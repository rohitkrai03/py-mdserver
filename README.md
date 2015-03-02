# Python Markdown Server

* It is a small python server based on markdown module which converts the .md file into html markup and serves it on the server on the fly. 
* It uses flask as its web framework.
* Its kind of a small blog where you can write your posts in text format and save it in docs folder. 
* All the files are then served to the server in .html format using the markdown module of python.
* There is also a feature of editing your posts via web pages using html forms. All the changes will be then saved to your .md files accordingly.


## How to Use

* Just download the package or clone the repo from github.
* Run the mdserve.py file. A server will be started on port 5000.
* Go to 

> http://localhost:5000/

* All the .md files which are in ../docs folder are converted into .html files and served on the server.
* Click on the Edit link in the webpage and you will be redirected to an HTML form where you can edit the document.
* If there is any directory inside of docs folder. Just type the directory name after the URL as follows: - 

> http://localhost:5000/stuff/

### Example : -
> py mdserve.py
