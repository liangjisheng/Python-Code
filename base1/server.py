
# socket server 服务端
# 我们使用socket模块的socket函数来创建一个socket对象。socket对象可以通过
# 调用其他函数来设置一个socket服务
# 现在我们可以通过调用bind(hostname, port)函数来指定服务的port(端口)
# 接着，我们调用socket对象的accept方法。该方法等待客户端的连接，
# 并返回connection对象，表示已连接到客户端

import sys, socket;

# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# 获取本地主机名
host = socket.gethostname();
port = 9999;

# 绑定端口
serversocket.bind((host, port));

# 设置最大连接数，超过后排队
serversocket.listen(5);

while True:	
	# 建立客户端连接
	clientsocket, addr = serversocket.accept();
	
	print("连接地址: %s" %str(addr));	
	msg = "欢迎使用socket，已经与服务器建立连接\r\n";
	clientsocket.send(msg.encode("utf-8"));
	clientsocket.close();