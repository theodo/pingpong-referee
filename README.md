# pingpong-referee

## Config

Edit the `index.html` and `server.py` to point to the right servers IP. In:
* `index.html`: the id of the http server handling requests (`server.py`)
* `server.py`: the id of the http server serving the sounds

Install the dependencies: `pip3 install soco`

## Launch

In the sounds directory: `python3 -m http.server <port>`
In the main directory: `./server.py`
