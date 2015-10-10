import webapp2
import jinja2
import base

class Admin(base.BaseHandler):
    def get(self):
        context = {'genre':self.load_ndb('genre'),'platform':self.load_ndb('platform')}
        self.render('admin.html',context)

    def post(self):
        action = self.request.get('action')
        message = ''
        if action == 'save':
            info = {'name':''}
            info['name'] = self.request.get('genre')
            if info['name']:
                self.store_ndb('genre', info)
                message = message + 'Added ' + info['name'] + ' to the database. '
            info['name'] = self.request.get('platform')
            if info['name']:
                self.store_ndb('platform', info)
                message = message + 'Added ' + info['name'] + ' to the database. '
            self.render('admin.html',{'message':message})
        else:
            self.render('admin.html',{'message':'Action ' + action + ' is unknown.'})
        
