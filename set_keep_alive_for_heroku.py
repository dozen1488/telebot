import os
import socket 
import time
from threading import Timer, Thread, Event

def _bind_port():
    socket = socket.socket()
    socket.bind(('0.0.0.0', int(os.environ["PORT"])))
    socket.listen(1)
    print('App bind port')

def _ping_google():
    def ping():
        os.system("ping -n 1 google.com")

    while True:
        ping()
        time.sleep(300)

def _set_reccuring_ping():
    thread = Thread(None, _ping_google)
    thread.start()

def set_keep_alive_for_heroku():
    if "PORT" in os.environ:
        _bind_port()
        _ping_google()