from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import urllib2
import subprocess
from os import path
from urlparse import urlparse
from urlparse import parse_qs

class SondeHandler(BaseHTTPRequestHandler):
        def do_GET(self):
                try:
                        self.send_response(200)
                        url=urlparse(self.path)
                        script=url.path
                        arg=["./script/"+script]
                        for key,value in parse_qs(url.query).items():
                                arg.append("-"+str(key))
                                arg.append(str(value[0]))
                        rep=self.execScript(arg)
                        self.send_header('Content-Type','text/html')
                except Exception, e:
                        self.send_response(500)
                        self.send_header('Content-Type','text/html')
                        rep="ERROR : "+str(e)
                        
                self.end_headers()
                self.wfile.write(rep)

        def execScript(self,arg):
                print arg
                value=str(subprocess.check_output(arg).strip())
                return value

class myHTTPServer(HTTPServer):

        def __init__(self, *args, **kw):
                self.port=args[0][1]
                HTTPServer.__init__(self, *args, **kw)
                self.stopHTTP=False

        def serve_forever(self):
                while ( self.stopHTTP == False):
                        self.handle_request()

       

class SondeHTTP():

        def __init__(self):
                self.port=8080
                print 'Start HTTP server on '+str(self.port)
                self.server = myHTTPServer(('',self.port),SondeHandler)
                self.server.serve_forever()
                print 'Stop HTTP server on '+str(self.port)
        
       
