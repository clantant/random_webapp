import webapp2
import jinja2
import base

class View(base.BaseHandler):
    def get(self):
        self.render('main.html')

