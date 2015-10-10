import webapp2
import os
import jinja2
import db_defs
from google.appengine.ext import ndb

# From class exercise, base handler and options
class BaseHandler(webapp2.RequestHandler):

# This defines jinja's environment
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True
        )
# This renders template with template_variables, a dictionary
    def render(self, template, template_variables={}):
        template = self.jinja2.get_template(template)
        self.response.write(template.render(template_variables))

# This loads items from the ndb, it takes an entity to load and returns a list of its contents
    def load_ndb(self, entity):
        if (entity == 'genre'):
            out = [{x} for x in db_defs.genre.query(ancestor=ndb.Key(db_defs.genre, self.app.config.get('base-key'))).fetch()]
        elif (entity == 'platform'):
            out = [{x} for x in db_defs.platform.query(ancestor=ndb.Key(db_defs.platform, self.app.config.get('base-key'))).fetch()]
        return out

# This stores items into the ndb, it takes an entity and a dictionary of information and stores it in the ndb with the ancestor base-key from config
    def store_ndb(self, entity, info):
        if (entity == 'genre'):
            k = ndb.Key(db_defs.genre, self.app.config.get('base-key'))
            item = db_defs.genre(parent=k)
        elif (entity == 'platform'):
            k = ndb.Key(db_defs.platform, self.app.config.get('base-key'))
            item = db_defs.platform(parent=k)

        item.name = info['name']
        item.put()
