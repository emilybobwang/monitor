# -*- coding: utf-8 -*-
'''
###################
#websocket  server
####################
'''
from sockjs.tornado import SockJSConnection
from app.tools.SysInfoMonitor import SysInfoMonitor
import json
class RealTimehandler(SockJSConnection):
     waiters = set()
# create connection
     def on_open(self,request):
         try:
             self.waiters.add(self)
         except Exception as e:
             print(e)

     def on_message(self,message):
         try:
             m = SysInfoMonitor()
             data = dict()
             if message == "system":
                 data = dict(
                     mem=m.meminfo(),
                     swap=m.swapinfo(),
                     cpu=m.cpuinfo(),
                     disk=m.diskinfo(),
                     net=m.netinfo(),
                     dt=m.dt()
                 )
             # send new message to all client
             self.broadcast(self.waiters, json.dumps(data))  # broadcast
         except Exception as e:
             print(e)

     def on_close(self):
         try:
             self.waiters.remove(self)
         except Exception as e:
             print(e)