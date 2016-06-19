#!/usr/bin/python3

import http.server
import time
import soco


SERVER_ADDRESS = ('', 8888)
sonos = soco.discover().pop()
print(sonos)
sonos.volume = 100


def main():
    http.server.HTTPServer(SERVER_ADDRESS, YTDownloadHTTPRequestHandler).serve_forever()


class YTDownloadHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        scores = self.path.split('/')
        sonos.play_uri('http://192.168.10.155:8000/%s_%s.mp3' % (scores[1], scores[2]))


if __name__ == '__main__':
    main()
