import os
import time
import urllib.request

from socket import socket 
from threading import Timer, Thread, Event

def _bind_port():
    env_socket = socket()
    env_socket.bind(('0.0.0.0', int(os.environ["PORT"])))
    env_socket.listen(1)
    print('App bind port')

def _ping_google():
    def ping():
        contents = urllib.request.urlopen("http://google.com").read()

    while True:
        ping()
        time.sleep(300)

def _set_reccuring_ping():
    thread = Thread(None, _ping_google)
    thread.start()

def set_keep_alive_for_heroku():
    if "PORT" in os.environ:
        _bind_port()
        _set_reccuring_ping()