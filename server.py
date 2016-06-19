#!/usr/bin/python3

import contextlib
import gtts
import http.server
import os
import soco
import urllib.parse


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SOUND_DIR = os.path.join(CURRENT_DIR, 'sounds')
SCORES_URI = 'http://192.168.10.155:8000'
SERVER_ADDRESS = ('', 8888)


def main():
    http.server.HTTPServer(SERVER_ADDRESS, YTDownloadHTTPRequestHandler).serve_forever()


class YTDownloadHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        quoted_text = self.path[1:]
        text = urllib.parse.unquote(quoted_text)
        sound_path = os.path.join(SOUND_DIR, '%s.mp3' % text)
        if os.path.exists(sound_path) is False:
            gtts.gTTS(text=text, lang='fr').save(sound_path)
        sonos.play_uri('%s/%s.mp3' % (SCORES_URI, quoted_text))
        self.send_response(200)


if __name__ == '__main__':
    sonos = soco.discover().pop()
    print(sonos)
    with contextlib.suppress(FileExistsError):
        os.mkdir(SOUND_DIR)
    main()
