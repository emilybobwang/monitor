# -*- coding: utf-8 -*-
'''
###################
#websocket  server
####################
'''
from sockjs.tornado import SockJSConnection
from app.tools.SysInfoMonitor import SysInfoMonitor
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
             self.broadcast(self.waiters,message)
         except Exception as e:
             print(e)

     def on_close(self):
         try:
             self.waiters.remove(self)
         except Exception as e:
             print(e)