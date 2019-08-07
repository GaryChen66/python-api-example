
# GLAMpipe API python examples
Some examples for GLAMpipe API usage with python

## running examples
Language detection project (language-detection-project.py) creates a new project, adds couple of documents, creates a language detection node and executes it.
    
    python language-detection-project.py

CSV read project creates a new project, adds CSV import node, uploads dataset of Helsinki City Orchestra, executes the import node (reads the file) and then shows top 10 composers.
dataset: http://www.hri.fi/fi/dataset/helsingin-kaupunginorkesterin-konsertit

    python csv-read-project.py

You can delete all test projects_

    python delete-test-projects.py

## requirements:
- You should have latest development version of [GLAMpipe](http://glampipe.org) installed and running on http://localhost:3000
- python "requests" module http://docs.python-requests.org/en/master/
- python "json" module
