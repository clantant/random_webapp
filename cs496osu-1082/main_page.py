import webapp2
import jinja2
import base

class View(base.BaseHandler):
    def get(self):
        context = {'results':{'video_shows':self.load_ndb('video_shows'),'videogames':self.load_ndb('videogames'),'video_movies':self.load_ndb('video_movies'),'video_anime':self.load_ndb('video_anime')}}
        self.render('main.html', context)

