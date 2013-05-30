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
                        arg=""
                        for key,value in parse_qs(url.query).items():
                                arg=arg+" -"+str(key)+" \""+str(value[0]+"\"")
                        rep=self.execScript("./script/"+script,arg)
                        self.send_header('Content-Type','text/html')
                except Exception, e:
                        self.send_response(500)
                        self.send_header('Content-Type','text/html')
                        rep="ERROR : "+str(e)
                        
                self.end_headers()
                self.wfile.write(rep)

        def execScript(self,file,arg):
                print file+" "+arg
                value=str(subprocess.check_output([file,arg]).strip())
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

        def __init__(self,writer):
                self.writer=writer
                self.port=8080
                self.writer.log('Start HTTP server on '+str(self.port))
                self.server = myHTTPServer(('',self.port),SondeHandler)
                self.server.serve_forever()
                self.writer.log('Stop HTTP server on '+str(self.port))
        
       
