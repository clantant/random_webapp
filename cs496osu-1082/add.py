import webapp2
import jinja2
import base

class Add(base.BaseHandler):
    def get(self):
        context={'genre':self.load_ndb('genre'),'platform':self.load_ndb('platform')}
        self.render('add_page.html', context)

    def post(self):
        context={'genre':self.load_ndb('genre'),'platform':self.load_ndb('platform')}
        action = self.request.get('action')
        message = ''
        if action == 'save':
            info = {'name':self.request.get('name'),'platform':self.request.get('platform'),'genre':[{x} for x in self.request.get_all('genre')],'priority':self.request.get('priority'),'episode':self.request.get('episode')}
            info['complete'] = self.request.get('complete')
            if info['complete'] == 'True':
                info['complete'] = True
            else:
                info['complete'] = False
            entity = self.request.get('media')
            self.store_ndb(entity, info)
            context['message'] = 'Added ' + info['name'] + ' to the database. '
        else:
            context['message'] = 'Action ' + action + ' is unknown.'
        self.render('add_page.html', context)
