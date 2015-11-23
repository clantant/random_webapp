import webapp2
import jinja2
import base

class Root(base.BaseHandler):
    def get(self):
        context = {}
        self.render("howto.html", context)
