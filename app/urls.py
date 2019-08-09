# -*- coding: utf-8 -*-
from sockjs.tornado import SockJSRouter
from app.views.views_index import  IndexHandler as index
from app.views.views_real_time import RealTimehandler as realtime
from tornado.web import asynchronous, RequestHandler

urls = [
    (r"/",index)
]+ SockJSRouter(realtime,"/real/time").urls