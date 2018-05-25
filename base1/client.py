
# 接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 12345
# socket.connect(hosname, port )方法打开一个TCP连接到主机为hostname端口为
# port的服务商。连接后我们就可以从服务端获取数据，
# 记住，操作完成后需要关闭连接

import sys, socket;

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# 获取本地主机名
host = socket.gethostname();

# 设置端口号
port = 9999;

# 连接服务，指定主机和端口
s.connect((host, port));

# 接受小于1024字节的数据
msg = s.recv(1024);

s.close();

print(msg.decode("utf-8"));