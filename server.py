# server.py
from wsgiref.simple_server import make_server # wsgi service
from hello import application

# set up a server, the IP is blank, port:8000, handle:application:
httpd = make_server('', 8000, application)
print("Serving HTTP on port 8000...")
# start to listening http request:
httpd.serve_forever()
