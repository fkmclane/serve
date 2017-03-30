import web, web.fancyindex, web.page, web.file

from serve import config, log

http = None

routes = {}
error_routes = {}


class IndexHandler(web.fancyindex.FancyIndexHandler):
    local = config.template + '/res'
    remote = '/res'
    fileidx = 0

    def index(self):
        with open(config.template + '/' + 'index.html', 'r') as file:
            self.index_template = file.read()

        with open(config.template + '/' + 'entry.html', 'r') as file:
            self.index_entry = file.read()

        self.index_content_type = 'text/html; charset=' + web.default_encoding

        return super().index()


class ErrorPage(web.page.PageErrorHandler):
    directory = config.template
    page = 'error.html'


routes.update(web.file.new(config.root, dir_index=True, handler=IndexHandler))
error_routes.update(web.page.new_error(handler=ErrorPage))


def start():
    global http

    http = web.HTTPServer(config.addr, routes, error_routes, log=log.httplog)
    http.start()


def stop():
    global http

    http.stop()
    http = None
