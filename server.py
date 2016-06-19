#!/usr/bin/python3

import http.server
import soco


SCORES_URI = 'http://192.168.10.155:8000'
SERVER_ADDRESS = ('', 8888)
sonos = soco.discover().pop()
print(sonos)


def main():
    http.server.HTTPServer(SERVER_ADDRESS, YTDownloadHTTPRequestHandler).serve_forever()


class YTDownloadHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        scores = self.path.split('/')
        sonos.play_uri('%s/%s_%s.mp3' % (SCORES_URI, scores[1], scores[2]))


if __name__ == '__main__':
    main()
