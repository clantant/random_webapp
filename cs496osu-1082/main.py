#!/usr/bin/env python
import webapp2

config = {'shows':'video_shows','games':'videogames','movies':'video_movies','anime':'video_anime','base-key':'bass'}

app = webapp2.WSGIApplication([
    ('/', 'main_page.View'),
    ('/home', 'main_page.View'),
    ('/edit', 'edit.Edit'),
    ('/add', 'add.Add'),
    ('/admin', 'admin.Admin'),
], debug=True, config=config)
