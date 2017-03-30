import log

from serve import config


servelog = log.Log(config.log)
httplog = log.HTTPLog(config.log, config.httplog)
