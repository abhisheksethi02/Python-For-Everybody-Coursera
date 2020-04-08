import socket

mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('http://data.pr4e.org/',80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\r\n\r'.encode()
mysocket.send(cmd)
while True:
    data=mysocket.recv(512)
    if (len(data)<1):
        break
    print(data.decode,end='')
mysocket.close()