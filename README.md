# pycat
汎用TCP/UDP接続コマンドラインツールNetcatをpythonに書き直したものです。  
サーバを立てることや、サーバに接続することが簡単にできます。  

This is a rewrite of Netcat, a general-purpose TCP/UDP connection command line tool, into python.  
It's easy to set up a server and connect to a server.  
# 使用方法(How to use)
```
server>python3 pycat.py -lp <対象のポート番号>
client>python3 pycat.py -c -t <対象のIPアドレス> -p <対象のポート番号>
```
```
server>python3 pycat.py -lp <port number>
client>python3 pycat.py -c -t <target IP address> -p <target port>
```

![screenshot](https://user-images.githubusercontent.com/52772923/81173356-e1abda00-8fda-11ea-8ee9-c592097d353b.png)
