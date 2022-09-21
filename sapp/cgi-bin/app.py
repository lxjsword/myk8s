#!/usr/bin/env python
# coding:utf-8

# **********************************************************
# * Author        : ryanxjli
# * Email         : ryanxjli@tencent.com
# * Create time   : 2022-09-16 16:03
# * Last modified : 2022-09-16 16:03
# * Filename      : app.py
# * Description   : 
# **********************************************************
import os

print('HTTP/1.1 200 OK')
print("Content-type:text/html")
print('\n')
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>简单的CGI 程序！</title>')
print('</head>')
print('<body>')
print('Recieved request from {}'.format(os.environ.get('REMOTE_ADDR', '')))
print('Interval: {}'.format(os.environ.get("INTERVAL", 0)))
print('USERNAME: {}'.format(os.environ.get("USERNAME", '')))
print('You have hit {}'.format(os.environ.get('SERVER_NAME', '')))
print('</body>')
print('</html>')

