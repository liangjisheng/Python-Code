
# CGI 目前由NCSA维护，NCSA定义CGI如下：
# CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在
# 服务器上如：HTTP服务器，提供同客户端HTML页面的接口

# 为了更好的了解CGI是如何工作的，我们可以从在网页上点击一个链接或URL的流程：
# 1、使用你的浏览器访问URL并连接到HTTP web 服务器。
# 2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，
# 如果存在返回文件的内容，否则返回错误信息。
# 3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息。

print ("Content-type:text/html")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
print ('</body>')
print ('</html>')