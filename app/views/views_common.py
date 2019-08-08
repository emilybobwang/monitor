# -*- coding: utf-8 -*-
import tornado.web

class CommonHandler(tornado.web.RequestHandler):

    def progress_status(self, val):
        data = ""
        if 0 <= val < 25:
            data = " bg-success"  # 绿色
        if 25 <= val < 50:
            data = ""
        if 50 <= val < 75:
            data = " bg-warning"  # 橙色
        if 75 <= val <= 100:
            data = " bg-danger"  # 红色
        return data