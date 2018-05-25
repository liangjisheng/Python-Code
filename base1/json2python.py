
# Python 数据结构转换为JSON
# JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。
# 它基于ECMAScript的一个子集。
# Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。
# 在json的编解码过程中，python 的原始类型与json类型会相互转换，

import json;

# python 字典类型转换为json对象
data = {"no":1, "name":"runoob", "url":"http://www.baidu.com"};

json_str = json.dumps(data);
print("python 原始数据: ", repr(data));
print("JSON 对象: ", json_str);

# 将 JSON 对象转换为 Python 字典
data1 = json.loads(json_str);
print("data1['name']: ", data1["name"]);
print("data1['url']: ", data1["url"]);