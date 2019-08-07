# -*- coding: utf-8 -*-
import tornado.web
class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
#        self.write("<h1>实时监控系统</h1>")
        self.render("index.html")