#-*- coding:utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import options,define

from app.configs import configs
from app.urls import urls


define("port", default=8000, type=int, help="Running port")

class CustomApplication(tornado.web.Application):
    def __init__(self):
        handlers =urls
        settings = configs
        super(CustomApplication, self).__init__(handlers=handlers, **settings)


def create_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(
        CustomApplication()
    )

    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    print('create_server ok')