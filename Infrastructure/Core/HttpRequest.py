import os
import tornado.ioloop
import tornado.web
from ..Session.SessionFactory import SessionFactory

class BaseRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = SessionFactory.get_session()