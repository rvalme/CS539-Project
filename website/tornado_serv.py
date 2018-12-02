import tornado.web
import tornado.httpserver
import os
from tornado.web import StaticFileHandler
import config
import tornado.websocket
import csv

def add_zip(csv_file='LinearRegression.csv'):
    zip_dict = {}
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            zip_dict[row[0].zfill(5)] = row[1] #zipcode is the key
    return zip_dict



class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()
    zip_dict = add_zip()

    def open(self):
        self.connections.add(self)

    def on_message(self, message):
        [client.write_message(self.zip_dict[message]) for client in self.connections]

    def on_close(self):
        self.connections.remove(self)

class Application(tornado.web.Application):
    def __init__(self):
        basedir = os.path.dirname(__file__)
        handlers = [
            (r"/", MainHandler),
            (r'/static/(.*)', StaticFileHandler, {'path':os.path.join(basedir, 'static')}),
            (r"/ws", SimpleWebSocket),
        ]
        settings = {
            "debug": True,
            "template_path": "web/",
            "static_path": os.path.join(os.path.dirname(__file__), "static")
        }
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


def main():
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(8888)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
