
# time

import time;

localtime = time.localtime(time.time());
print("本地时间: ", localtime);

lt1 = time.asctime(localtime);
print("本地时间: ", localtime);

# 可以使用time模块的strtime方法来格式化日期
# time.strftime(format[, t])

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


# 打印某月的月历
import calendar

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)