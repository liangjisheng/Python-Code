
s = "11abc22abc33abc44abc55";
print(s);
s = s.replace("abc", "ABC");
print(s);

s = s.replace("ABC", "");
print(s);

# 网址加载到浏览器里
import webbrowser as web;
url = "https://www.baidu.com/?tn=93380420_hao_pg";
web.open_new_tab(url);

url = " http://www.tudou.com/programs/view/myLEA7IrHx4/"
web.open_new_tab(url);

# 关闭浏览器
import os;
import time;

time.sleep(1);
os.system("taskkill /F /IM chrome.exe");