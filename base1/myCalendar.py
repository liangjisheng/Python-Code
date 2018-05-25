
# 生成日历

import calendar;		# 日历模块

yy = int(input("输入年份: "));
mm = int(input("输入月份: "));

# 显示日历
print(calendar.month(yy, mm));

# 计算每个月的天数
# 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几(0-6)
# 第二个元素是这个月的天数。以上实例输出的意思为2016年9月份的第一天
# 是星期四，该月总共有30天
monthrange = calendar.monthrange(2016, 9);
print(monthrange);

print(calendar.mdays[9]);