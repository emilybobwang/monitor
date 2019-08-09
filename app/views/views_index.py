# -*- coding: utf-8 -*-
import tornado.web
from app.tools.SysInfoMonitor import SysInfoMonitor
from app.tools.chart import Chart
from app.views.views_common import  CommonHandler

class IndexHandler(CommonHandler):
    def get(self,*args,**kwargs):
        cpu_info = SysInfoMonitor().cpuinfo()
#        self.write("<h1>实时监控系统</h1>")
        self.render("index.html",
                    data = dict(
                            cpu_info = cpu_info,
                            cpu_liquid= Chart().liqiud_html("cpu_avg","CPU usage",cpu_info['percent_avg'])
                    )
                    )