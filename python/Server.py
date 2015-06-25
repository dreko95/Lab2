__author__ = 'Lecks'

import pydoc
import time
from bottle import run, get, post, debug, static_file, request
from functions import Bartender


# Displays server data html page for request localhost:8081/server
@get('/')
def server():

    return static_file('Server.html', root='../static/')


# Displays worker data html page for request localhost:8081/worker
@get('/client')
def worker():
    return static_file('Client.html', root='../static/')


# Returns static file. Used for getting JavaScript files from /static folder
@get('/static/:filename#.*#')
def get_static(filename):
    return static_file(filename, root='../static/')


# Returns static file. Used for getting JavaScript files from /scripts folder
@get('/scripts/:filename#.*#')
def get_scripts(filename):
    return static_file(filename, root='../scripts/')


#Returns static file. Used for getting JavaScript files from /js folder
@get('/js/:filename#.*#')
def get_js(filename):
    return static_file(filename, root='../js/')


# Returns global server variables when /ServerData is requested
@get('/ServerData')
def get_server_data():
    return {'percent': h.percent, 'clients': h.clients, 'time': h.time, 'result': h.result}


# Receives data from Server.js through request key
@post('/ServerData')
def post_server_data():
    print "good"


# We give the signal for the continuation of robots and vydilyaem next subtext to check
@get('/ClientData')
def get_client_data():

    if h.counter >= len(h.tasks):
        h.set_time(time.time() - t)
        print "Calculation is done"
        return {'state': 'STOP'}
    h.sent_parts += 1
    return {'state': 'WORK', 'task': h.get_task(), 'full_text': h.full_text}


# We receive data after processing employee
@post('/ClientData')
def post_client_data():

    h.received_parts += 1 #: doccomment for class attribute
    h.clients = h.sent_parts - h.received_parts - 1

    h.percent = int(100 * h.counter / len(h.tasks))
    h.result += int(request.forms.get('result'))

#__main__
if __name__ == '__main__':
    t = time.time()
    h = Bartender('WORK')
    h.form_tasks()
    run(port=8081)#run
