import webapp2
import jinja2
import base
from google.appengine.ext import ndb

class Edit(base.BaseHandler):
    def get(self):
        action = self.request.get('type')
        if action == 'delete':
            item_key = ndb.Key(urlsafe=self.request.get('key'))
            item_name = item_key.get()
            item_name = item_name.name
            item_key.delete()
            context = {'message':'Deleted ' + item_name + ' from the database.'}
        elif action == 'edit':
            item_key = ndb.Key(urlsafe=self.request.get('key'))
            item = item_key.get()
            checks = {}
            context = {'info':item}
            context['genre'] = self.load_ndb('genre')
            context['platform'] = self.load_ndb('platform')
            checks['platform_check'] = item.platform
            for x in item.genre:
                checks['genre_check'] = {x:'checked'}
            checks['key_check'] = item.key.urlsafe()
            context.update(checks)
        else:
            context = {'results':{'video_shows':self.load_ndb('video_shows'),'videogames':self.load_ndb('videogames'),'video_movies':self.load_ndb('video_movies'),'video_anime':self.load_ndb('video_anime')}}
            results = context['results']
            keys = {}
            for entity,value in results.items():
                for item in value:
                    keys[item.name] = item.key.urlsafe()
            context['keys'] = keys
        self.render('edit_page.html', context)

    def post(self):
        item_key = ndb.Key(urlsafe=self.request.get('key'))
        action = self.request.get('action')
        if action == 'save':
            info = {'name':self.request.get('name'),'platform':self.request.get('platform'),'genre':[{x} for x in self.request.get_all('genre')],'priority':self.request.get('priority'),'episode':self.request.get('episode')}
            info['complete'] = self.request.get('complete')
            if info['complete'] == 'True':
                info['complete'] = True
            else:
                info['complete'] = False
            item = item_key.get()
            item.name = info['name']
            item.platform = info['platform']
            genre = []
            for x in info['genre']:
                genre.append(''.join(x))
            item.genre = genre
            item.priority = int(info['priority'])
            if info['episode']:
                item.episode = int(info['episode'])
            item.complete = info['complete']
            item.put()
        context = {'message':'Modified ' + item.name + ' in the database.'}
        self.render('edit_page.html',context)

