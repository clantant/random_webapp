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
# If you add a new entity, load it here.
    def load_ndb(self, entity):
        if (entity == 'genre'):
            out = db_defs.genre.query(ancestor=ndb.Key(db_defs.genre, self.app.config.get('base-key'))).fetch()
        elif (entity == 'platform'):
            out = db_defs.platform.query(ancestor=ndb.Key(db_defs.platform, self.app.config.get('base-key'))).fetch()
        elif (entity == 'video_shows'):
            out = db_defs.video_shows.query(ancestor=ndb.Key(db_defs.video_shows, self.app.config.get('base-key'))).fetch()
        elif (entity == 'videogames'):
            out = db_defs.videogames.query(ancestor=ndb.Key(db_defs.videogames, self.app.config.get('base-key'))).fetch()
        elif (entity == 'video_movies'):
            out = db_defs.platform.query(ancestor=ndb.Key(db_defs.video_movies, self.app.config.get('base-key'))).fetch()
        elif (entity == 'video_anime'):
            out = db_defs.platform.query(ancestor=ndb.Key(db_defs.video_anime, self.app.config.get('base-key'))).fetch()
        return out

# This stores items into the ndb, it takes an entity and a dictionary of information and stores it in the ndb with the ancestor base-key from config
# If you add a new entity, give it a storage method here.
    def store_ndb(self, entity, info):
        if (entity == 'genre'):
            _store_genre(info)
        elif (entity == 'platform'):
            _store_platform(info)
        elif (entity == 'video_shows'):
            _store_video_shows(info)
        elif (entity == 'videogames'):
            _store_videogames(info)
        elif (entity == 'video_movies'):
            _store_video_movies(info)
        elif (entity == 'video_anime'):
            _store_video_anime(info)


    def _store_video_shows(self, info):
        k = ndb.Key(db_defs.video_shows, self.app.config.get('base-key'))
        item = db_defs.video_shows(parent=k)
        item.name = info['name']
        item.platform = info['platform']
        item.complete = info['complete']
        item.genre = info['genre']
        item.episode = info['episode']
        item.priority = info['priority']
        item.put()


    def _store_videogames(self, info):
        k = ndb.Key(db_defs.videogames, self.app.config.get('base-key'))
        item = db_defs.videogames(parent=k)
        item.name = info['name']
        item.platform = info['platform']
        item.complete = info['complete']
        item.genre = info['genre']
        item.priority = info['priority']
        item.put()


    def _store_video_movies(self, info):
        k = ndb.Key(db_defs.video_movies, self.app.config.get('base-key'))
        item = db_defs.video_movies(parent=k)
        item.name = info['name']
        item.platform = info['platform']
        item.complete = info['complete']
        item.genre = info['genre']
        item.priority = info['priority']
        item.put()


    def _store_video_anime(self, info):
        k = ndb.Key(db_defs.video_anime, self.app.config.get('base-key'))
        item = db_defs.video_anime(parent=k)
        item.name = info['name']
        item.platform = info['platform']
        item.complete = info['complete']
        item.genre = info['genre']
        item.episode = info['episode']
        item.priority = info['priority']
        item.put()


    def _store_genre(self, info):
        k = ndb.Key(db_defs.genre, self.app.config.get('base-key'))
        item = db_defs.genre(parent=k)
        item.name = info['name']
        item.put()


    def _store_platform(self, info):
        k = ndb.Key(db_defs.platform, self.app.config.get('base-key'))
        item = db_defs.platform(parent=k)
        item.name = info['name']
        item.put()
