
import tornado.ioloop
import tornado.web
import tornado.websocket
import sys

import services.filesystem


class MainPageHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello from the MainPageHandler! :D")

		
class ShutdownHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Shutting down")
		sys.exit("Forced Shutdown")

if __name__ == "__main__":

	print 'Registering handlers'

	# Register handlers for various page requests
	application = tornado.web.Application([
		(r"/", MainPageHandler),
		(r"/files/(.*)", services.filesystem.FilesHandler),
		(r"/directories/(.*)", services.filesystem.DirectoriesHandler),
		(r"/suggestion/(.*)", services.filesystem.SuggestionHandler),
		(r"/browse/(.*)", services.filesystem.BrowseHandler),
		# (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/home/chase/static_www"}),
		(r"/shutdown", ShutdownHandler),
	], debug=True)
	
	print 'Setting up listener'
	application.listen(50006)
	
	print 'Starting ioloop'
	tornado.ioloop.IOLoop.instance().start()
	