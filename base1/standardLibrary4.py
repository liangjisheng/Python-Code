
# datetime模块为日期和时间处理同时提供了简单和复杂的方法。
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
# 该模块还支持时区处理:
# dates are easily constructed and formatted

from datetime import date;

now = date.today();
print(now);

res = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B");
print(res);
print();

# dates support calendar arithmetic
birthday = date(1964, 7, 31);
age = now - birthday;
print(age.days);


# 以下模块直接支持通用的数据打包和压缩格式：
# zlib，gzip，bz2，zipfile，以及 tarfile

import zlib;

s = b"witch which has which witches wrist watch";
print(s);
print(len(s));

t = zlib.compress(s);
print(t);
print(len(t));

de = zlib.decompress(t);
print(de);

print(zlib.crc32(s));