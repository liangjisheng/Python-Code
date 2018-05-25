
# 网络模块
# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于
#处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的smtplib

from urllib.request import urlopen;

for line in urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl"):
	line = line.decode("utf-8");	# Decoding the binary data to text.
	if "EST" in line or "EDT" in line : # look for Eastern Time
		print(line);