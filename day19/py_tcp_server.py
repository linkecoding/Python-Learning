# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import time

# # 创建一个socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接
# s.connect(('www.sina.com.cn', 80))
# # 发送数据
# s.send(b'GET / HTTP/1.1 \r\nHost: www.sina.com.cn\r\n\
#     Connection: keep-alive\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     # 每次最多接收1k字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break

# data = b''.join(buffer)
# # 关闭连接
# s.close()
# # 接收到的数据包括HTTP头和网页本身
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把网页数据写入文件
# with open('sina.html', 'wb') as f:
#     f.write(html)

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听端口
s.bind(('127.0.0.1', 9999))
# 开始监听(指定等待连接的最大连接数)
s.listen(5)
print('waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)


# 开始处理连接
while True:
    # 接收一个新的连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
