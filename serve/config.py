import json as _json
import logging as _logging
import os as _os
import os.path as _path
import sys as _sys

import fooster.web as _web


# address to listen on
addr = ('', 8000)

# log locations
log = '/var/log/serve/serve.log'
http_log = '/var/log/serve/http.log'

# template directory to use
template = _path.dirname(__file__) + '/html'

# root directory of files to serve
root = '/var/www/serve'


# store config in env var
def _store():
    config = {key: val for key, val in globals().items() if not key.startswith('_')}

    _os.environ['SERVE_CONFIG'] = _json.dumps(config)


# load config from env var
def _load():
    config = _json.loads(_os.environ['SERVE_CONFIG'])

    globals().update(config)

    # automatically apply
    _apply()


# apply special config-specific logic after changes
def _apply():
    # setup logging
    if log:
        _logging.getLogger('serve').addHandler(_logging.FileHandler(log))
    else:
        _logging.getLogger('serve').addHandler(_logging.StreamHandler(_sys.stdout))

    if http_log:
        http_log_handler = _logging.FileHandler(http_log)
        http_log_handler.setFormatter(_web.HTTPLogFormatter())

        _logging.getLogger('http').addHandler(http_log_handler)

    # automatically store if not already serialized
    if 'SERVE_CONFIG' not in _os.environ:
        _store()


# load if config already serialized in env var
if 'SERVE_CONFIG' in _os.environ:
    _load()
