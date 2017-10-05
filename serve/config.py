# address to listen on
addr = ('', 8080)

# log locations
log = '/var/log/serve/serve.log'
http_log = '/var/log/serve/http.log'

# template directory to use
import os.path
template = os.path.dirname(__file__) + '/html'

# root directory of files to serve
root = '/var/www/serve'
