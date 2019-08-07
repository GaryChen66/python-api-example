

'''
This is an example application for using GLAMpipe API.
Application creates a project, adds some documents to it and detects language of 'text' field
'''

import requests
import json
url = "http://localhost:3000/api/v1"


def deleteTestProjects():
	r = requests.get(url + "/projects/titles")
	parsed = json.loads(r.text)
	for p in parsed:
		if "Python" in p['title']:
			c = requests.delete(url + "/projects/" + p['_id'])
			print("Deleted " + p['title'])



# delete all test projects
deleteTestProjects()

