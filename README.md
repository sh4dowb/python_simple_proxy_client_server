# Python Simple Proxy Client & Server

A simple TCP proxy script.

  - ROT13 encoding (to bypass some firewalls, like my school's)
  - Reads request from pipe
  - One connection at one time
  - Uses Python sockets
  - Absolutely unsecure & useless


# Few examples to this useless thing

**Client**
```
sh4dow@laptop:~$ cat request.txt | python simpleproxy-client.py 127.0.0.1 9999
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 28 Dec 2017 18:12:55 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 34
Connection: keep-alive
Keep-Alive: timeout=60

Hey, this is a web server.
sh4dow@laptop:~$ echo "127.0.0.1:1234/hey netcat on port 1234 how are you" |
> python simpleproxy-client.py 127.0.0.1 9999
fine thanks

sh4dow@laptop:~ $ 
```

**Server**
```
sh4dow@laptop:~$ python simpleproxy-server.py 9999
Listening on 0.0.0.0:9999
Connection from 127.0.0.1
Received request from client
Sent request
Received response
Sent response to client
Connection closed

Connection from 127.0.0.1
Received request from client
Sent request
Received response
Sent response to client
Connection closed
```

**request.txt**
```
127.0.0.1:80/GET / HTTP/1.1
Host: example.com

```
