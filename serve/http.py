import os.path

import fooster.web
import fooster.web.fancyindex
import fooster.web.page
import fooster.web.file

from serve import config


http = None

routes = {}
error_routes = {}


class IndexHandler(fooster.web.fancyindex.FancyIndexHandler):
    def index(self):
        with open(os.path.join(config.template, 'index.html'), 'r') as file:
            self.index_template = file.read()

        with open(os.path.join(config.template, 'entry.html'), 'r') as file:
            self.index_entry = file.read()

        self.index_content_type = 'text/html; charset=' + fooster.web.default_encoding

        return super().index()


class ErrorPage(fooster.web.page.PageErrorHandler):
    directory = config.template
    page = 'error.html'


routes.update(fooster.web.file.new(config.root, dir_index=True, handler=IndexHandler))
error_routes.update(fooster.web.page.new_error(handler=ErrorPage))


def start():
    global http

    http = fooster.web.HTTPServer(config.addr, routes, error_routes)
    http.start()


def stop():
    global http

    http.stop()
    http = None


def join():
    global http

    http.join()
