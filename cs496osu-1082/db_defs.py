from google.appengine.ext import ndb

class video_shows(ndb.Model):
    name = ndb.StringProperty(required=True)
    platform = ndb.StringProperty(required=True)
    complete = ndb.BooleanProperty(required=True)
    genre = ndb.StringProperty(repeated=True)
    episode = ndb.IntegerProperty()
    priority = ndb.IntegerProperty()

class videogames(ndb.Model):
    name = ndb.StringProperty(required=True)
    platform = ndb.StringProperty(required=True)
    complete = ndb.BooleanProperty(required=True)
    genre = ndb.StringProperty(repeated=True)
    priority = ndb.IntegerProperty()

class video_movies(ndb.Model):
    name = ndb.StringProperty(required=True)
    platform = ndb.StringProperty(required=True)
    complete = ndb.BooleanProperty(required=True)
    genre = ndb.StringProperty(repeated=True)
    priority = ndb.IntegerProperty()

class video_anime(ndb.Model):
    name = ndb.StringProperty(required=True)
    platform = ndb.StringProperty(required=True)
    complete = ndb.BooleanProperty(required=True)
    genre = ndb.StringProperty(repeated=True)
    episode = ndb.IntegerProperty()
    priority = ndb.IntegerProperty()

class genre(ndb.Model):
    name = ndb.StringProperty(required=True)

class platform(ndb.Model):
    name = ndb.StringProperty(required=True)
