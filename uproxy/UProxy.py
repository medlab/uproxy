#!/bin/bash -c 'env python3'

"""Tiny HTTP Proxy.

This module implements GET, HEAD, POST, PUT and DELETE methods
on BaseHTTPServer, and behaves as an HTTP proxy.  The CONNECT
method is also implemented experimentally, but has not been
tested yet.

Any help will be greatly appreciated.           SUZUKI Hisao

---------------------------------------------------------------
Adjust by Cong Zhang:

rewrite some socket related part to make ipv4/ipv6 auto adjust
force to work with only python3
"""

import argparse
import select
import socket
import socketserver
import http.server
import urllib.parse

def be_sure_to_bytes(str_or_bytes):
    return str_or_bytes if str is bytes else str_or_bytes.encode('utf-8')
    pass

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    __base = http.server.BaseHTTPRequestHandler
    __base_handle = __base.handle

    server_version = "TinyHTTPProxy Alpha"
    rbufsize = 0  # self.rfile Be unbuffered

    def handle(self):
        (ip, port) = self.client_address
        if hasattr(self, 'allowed_clients') and ip not in self.allowed_clients:
            self.raw_requestline = self.rfile.readline()
            if self.parse_request(): self.send_error(403)
        else:
            self.__base_handle()

    def _connect_to(self, netloc):
        i = netloc.find(':')
        if i >= 0:
            host_port = netloc[:i], int(netloc[i + 1:])
        else:
            host_port = netloc, 80
        print(("\t" "connect to %s:%d" % host_port))
        try:
            return socket.create_connection(host_port)
        except socket.error as arg:
            try:
                msg = arg[1]
            except:
                msg = arg
            self.send_error(404, msg)
            return None
            # return None

    def do_CONNECT(self):
        # soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            soc = self._connect_to(self.path);
            if not soc is None:
                self.log_request(200)
                self.wfile.write(be_sure_to_bytes(self.protocol_version +
                                 " 200 Connection established\r\n"))
                self.wfile.write(be_sure_to_bytes("Proxy-agent: %s\r\n" % self.version_string()))
                self.wfile.write(b"\r\n")
                self._read_write(soc, 300)
        finally:
            print("\t" "bye")
            if not soc is None:
                soc.close()
            self.connection.close()

    def do_GET(self):
        (scm, netloc, path, params, query, fragment) = urllib.parse.urlparse(
            self.path, 'http')
        if scm != 'http' or fragment or not netloc:
            self.send_error(400, "bad url %s" % self.path)
            return
        # soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # soc=socket.create_connection()
            soc = self._connect_to(netloc)
            if not soc is None:
                self.log_request()
                soc.send(be_sure_to_bytes("%s %s %s\r\n" % (
                    self.command,
                    urllib.parse.urlunparse(('', '', path, params, query, '')),
                    self.request_version)))
                self.headers['Connection'] = 'close'
                del self.headers['Proxy-Connection']
                for key_val in list(self.headers.items()):
                    soc.send(be_sure_to_bytes("%s: %s\r\n" % key_val))
                soc.send(b"\r\n")
                self._read_write(soc)
        finally:
            print("\t" "bye")
            if not soc is None:
                soc.close()
            self.connection.close()

    def _read_write(self, soc, max_idling=200):
        iw = [self.connection, soc]
        ow = []
        count = 0
        while 1:
            count += 1
            (ins, _, exs) = select.select(iw, ow, iw, 3)
            if exs: break
            if ins:
                for i in ins:
                    if i is soc:
                        out = self.connection
                    else:
                        out = soc
                    data = i.recv(8192)
                    if data:
                        out.send(data)
                        count = 0
            else:
                print(("\t" "idle", count))
            if count == max_idling: break

    do_HEAD = do_GET
    do_POST = do_GET
    do_PUT = do_GET
    do_DELETE = do_GET


class ThreadingHTTPServer(socketserver.ThreadingMixIn,
                          http.server.HTTPServer):
    pass


class ForkHTTPServer(socketserver.ThreadingMixIn,
                     http.server.HTTPServer):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='127.0.0.1', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    parser.add_argument('--allowed-ip', default=None,
                        help='Filter which client you want serve for!')
    args = parser.parse_args()

    if args.allowed_ip is not None:
        allowed = []

        client = socket.gethostbyname(args.allowed_ip)
        allowed.append(client)
        print("Accept: %s (%s)" % (client, args.allowed_ip))

        ProxyHandler.allowed_clients = allowed
    else:
        print("Any clients will be served...")

    http.server.test(ProxyHandler, ForkHTTPServer, port=args.port, bind=args.bind)
    pass


if __name__ == '__main__':
    main()
