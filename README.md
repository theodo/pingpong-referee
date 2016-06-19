# pingpong-referee

## Config

Edit the `index.html` and `server.py` to point to the right servers URIs. In:
* `index.html`: the URI of the http server handling requests (`server.py`)
* `server.py`: the URI of the http server serving the sounds

Install the dependencies: `pip3 install -r requirements.txt`

## Launch

In the sounds directory: `python3 -m http.server <port>`

In the main directory: `./server.py`
