
from aip import AipImageClassify;
"""你的 APPID AK SK"""
APPID = '10943873';
API_KEY = 'B7e2zqQAkO7ZbBqjioZMYHSG';
SECRET_KEY = 'aThvZW6Qvoc0CXMG8YafZCDN2kQZMG0j';

client = AipImageClassify(APPID, API_KEY, SECRET_KEY);

"""读取图片"""
def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read();
		
image = get_file_content('test.jpg');

"""调用车辆识别"""
# options={"top_num":1}代表返回的多个可能车型中的第一个
print(client.carDetect(image, options = {"top_num":1})["result"][0]["name"]);
print();

print(client.carDetect(image, options = {"top_num":1})["result"][0]);
print();

print(client.carDetect(image, options = {"top_num":1})["result"]);
print();

print(client.carDetect(image, options = {"top_num":1}));
print();

print(client.carDetect(image));

print(len(list((client.carDetect(image)).keys())));