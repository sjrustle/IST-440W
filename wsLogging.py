#From WebPy

import sys, logging
from wsgilog import WsgiLog
import config

#Log class, logs all HTTP requests this includes POSTS/GETS
class Log(WsgiLog):
    def __init__(self, application):
        WsgiLog.__init__(
            self,
            application,
            logformat = '%(message)s',
            tofile = True,
            toprint = True,
            #Configure the log_file, with the config module
            file = config.log_file,
            interval = config.log_interval,
            backups = config.log_backups
            )