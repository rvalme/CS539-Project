import tornado.web
import tornado.httpserver
import os
from tornado.web import StaticFileHandler
import tornado.websocket
import csv

def add_zip(msg, csv_file='data.csv'):
    zip_dict = {}
    dtype = msg.split('|')[1]
    with open(dtype + csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            zip_dict[row[0].zfill(5)] = row[2] + '|' + row[1] #zipcode is the key 1 is the actual 2 is the predicted
    return zip_dict



class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()
    zip_dict = {}

    def open(self):
        self.connections.add(self)

    def on_message(self, message):
        self.zip_dict = add_zip(message)
        try:
            wrmsg = self.zip_dict[message.split('|')[0]]
        except:
            wrmsg = '0|0'
        [client.write_message(wrmsg) for client in self.connections]

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
    port = int(os.getenv('PORT',4200))
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(port)
    http_server.listen(8888)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
