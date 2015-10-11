import webapp2
import jinja2
import base

class Edit(base.BaseHandler):
    def get(self):
        self.render('edit_page.html')

    def post(self):
        self.render('edit_page.html')
