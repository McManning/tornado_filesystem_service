
# webfilesystem.py

import tornado.web
import os
import ConfigParser
import re

def get_files(path):
	filenames = []
	
	config = ConfigParser.RawConfigParser()
	config.optionxform = str # enable case sensitivity on option strings
	config.read('filesystem.ini')
	
	# Ignore root, there are only virtual folders
	if len(path) > 0:
		# extract and expand the root virtual path to an actual path
		plist = path.split('/')
		vroot = plist.pop(0)
		path = '/'.join(plist)
		
		root = config.get('virtual_roots', vroot)
	
		for (dirpath, directories, filenames) in os.walk(root + path):
			break	

	return filenames
	
	
def get_directories(path):

	directories = []

	config = ConfigParser.RawConfigParser()
	config.optionxform = str # enable case sensitivity on option strings
	config.read('filesystem.ini')
	
	# if at root, return a configured list of virtual root folders
	if len(path) < 1:
		directories = config.options('virtual_roots')
	
	else:
		# extract and expand the root virtual path to an actual path
		plist = path.split('/')
		vroot = plist.pop(0)
		path = '/'.join(plist)
		
		root = config.get('virtual_roots', vroot)
	
		for (dirpath, directories, filenames) in os.walk(root + path):
			break
	
	return directories
	
		
class FilesHandler(tornado.web.RequestHandler):
	def get(self, path):
	
		json_response = {
			'path': path,
			'path_split': path.split('/'),
			'files': get_files(path)
		}
		
		self.write(json_response)
	
		
class DirectoriesHandler(tornado.web.RequestHandler):
	def get(self, path):
		
		json_response = {
			'path': path,
			'path_split': path.split('/'),
			'directories': get_directories(path)
		}
		
		self.write(json_response)
		
class BrowseHandler(tornado.web.RequestHandler):
	def get(self, path):
		
		# clean up trailing slashes in path
		if len(path) > 0 and path[-1] == '/': 
			path = path[:-1]
		
		self.render('views/browse.pyhtm', 
			path = path,
			files = get_files(path),
			directories = get_directories(path)
		)
		
class SuggestionHandler(tornado.web.RequestHandler):
	def get(self, path):
		# /suggestion/path/to/stuff?file=blah.pdf
		
		filename = self.get_argument('file', None)
		
		target = ''
		
		if filename:
			
			config = ConfigParser.RawConfigParser()
			config.optionxform = str # enable case sensitivity on option strings
			config.read('filesystem.ini')
			
			path = path + '/' + filename
			for regex in config.options('move_suggestions'):
				if re.match(regex, path):
					target = config.get('move_suggestions', regex)
					break
			
		json_response = {
			'suggestion': target
		}
		self.write(json_response)

		
