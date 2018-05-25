
from urllib import request;

# 打开网站
response = request.urlopen("http://www.baidu.com");
# 打卡文件
fi = open("test.txt", "w");
# 网站代码写入
page = fi.write(str(response.read()));
fi.close();

# input()默认输入格式为str
a = input("请输入数字: ");
print(a * 2);
a = int(input("请输入数字: "));
print(a * 2);

input();