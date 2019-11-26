# coding=utf-8

import socketserver

class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        print(data)
        self.request.send(bytes("HTTP/1.1 2OO\r\n", "utf-8"))
        self.request.send(bytes("\r\n", "utf-8"))
        self.request.send(bytes("hello world", "utf-8"))


server = socketserver.TCPServer(("", 8080), MyHandler)
server.serve_forever()
