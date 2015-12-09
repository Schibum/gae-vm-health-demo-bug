import threading
import logging
import time

import webapp2
from webapp2 import Route


class HealthCheckHandler(webapp2.RequestHandler):
    def get(self):
        status = 'this is the custom handler'
        logging.info('status: %s', status)
        self.response.write(status)


class StartHandler(webapp2.RequestHandler):
    def get(self):
        # start thread etc.
        self.response.write('status ok')


app = webapp2.WSGIApplication(
    [Route('/_ah/health', HealthCheckHandler),
     Route('/_ah/start', StartHandler),
    ], debug=False)

if __name__ == '__main__':
    from wsgiref import simple_server
    simple_server.make_server('', 8080, app).serve_forever()
