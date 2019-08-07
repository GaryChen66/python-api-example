

'''
This is an example application for using GLAMpipe API.
Application creates a project, adds some documents to it and detects language of 'text' field
'''

import requests
import json
url = "http://localhost:3000/api/v1"

def createProject(title):
	print('Creating project ' + title)
	title = "Python: " + title
	payload = {'title': title}
	r = requests.post(url + "/projects", data=payload)
	#print(r.text)
	parsed = json.loads(r.text)
	return parsed['project']['_id']

def createCollection(project):
	data = {'params': {'title':  'my collection'}}
	print('Adding collection to project')
	r = requests.post(url + "/projects/" + project + "/nodes/collection_basic?type=collection", json=data)
	parsed = json.loads(r.text)
	return parsed['collection']


def deleteTestProjects():
	r = requests.get(url + "/projects/titles")
	parsed = json.loads(r.text)
	for p in parsed:
		if "Python" in p['title']:
			c = requests.delete(url + "/projects/" + p['_id'])
			print("Deleted " + p['title'])

def addDocument(doc, collection):
	print("Add document to collection '" + collection + "'")
	r = requests.post(url + "/collections/" + collection + "/docs/", json=doc)

def addNode(nodetype, params, project):
	print("adding node '" + nodetype + "'")
	r = requests.post(url + "/projects/" + project + "/nodes/" + nodetype, json=params)
	parsed = json.loads(r.text)
	return parsed['id']

def runNode(node_id, settings):
	print("running node " + node_id)
	r = requests.post(url + "/nodes/" + node_id + "/run", json=settings)

def getAllDocs(collection):
	r = requests.get(url + "/collections/" + collection + "/docs")
	return json.loads(r.text)
	

# main program
project_id = createProject("language detection")
collection_id = createCollection(project_id)

# add some data
doc = {'title': 'My first document', 'author': 'Linus Torvalds','text': 'This is an english text, right?'}
addDocument(doc, collection_id);
doc = {'title': 'My second document', 'author': 'Joulupukki','text': 'Suomi on kaunis kieli, onhan?'}
addDocument(doc, collection_id);

# add text detection node
params = {'in_field': 'text', 'out_field': 'text_detected_lang'}
data = {'params': params, 'collection': collection_id}
text_detection = addNode('process_field_detect_language', data, project_id);

# run text detection node
settings = {'settings': {}}
runNode(text_detection, settings)

# get result
docs = getAllDocs(collection_id)
print('\n************ LANGUAGE DETECTION ****************')
for doc in docs['data']:
	print(doc['text'] + ' -> ' + doc['text_detected_lang'][0]) # note that node outputs an array
print('************************************************\n')


# uncomment this to delete all python test projects
#deleteTestProjects()

