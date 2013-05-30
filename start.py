#!/usr/bin/python
from sondeWriter import *
from time import sleep
from sondeHTTP import *
import sondeWriter

class Domopy:
        def __init__(self):
                writer = SondeWriter()
                #Start HTTP
                http=SondeHTTP(writer)

if __name__ == "__main__":
        domopy=Domopy()
