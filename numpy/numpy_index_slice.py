# -*- coding:utf-8 -*-
"""
@project = 0713-1
@file = numpy_index_slice
@author = Liangjisheng
@create_time = 2018/7/13 0013 下午 14:58
"""
import numpy as np
# 在索引中出现冒号(:)，则本轴继续存在，如果只是一个数值，则本轴消失
# 像 :, :1, 1: 这样的索引，保留此轴， data[:, :1, 2:] 中，三个轴都保留
# data[1, 4, 2] 三个轴都消失，只返回一个数值
# data[1:2, 0:1, 0:1] 中，三个轴都保留，但只有一个数据元素

data = np.arange(24).reshape(2, 3, 4)
print(data)
# axis 0，即z轴，是数值，则z轴消失，切了一片x-y
print(data[0, :, :])
# 所有轴都消失，只返回一个标量数据
print(data[0, 1, 2])
# 返回三维数据，虽然只有一个元素
print(data[0:1, 1:2, 2:3])
print()

# 拼接（concatenating）指定哪个轴，就在哪个轴向拼接
d1 = np.arange(4).reshape(2, 2)
# 在轴向 0 拼接，即 y 方向
print(np.concatenate([d1, d1], axis=0))
# 在轴向 1 拼接，即 x 方向
print(np.concatenate([d1, d1], axis=1))

# ndarray 的数据在内存里以一维线性存放，reshape前后，数据没有变化，只是访问方式变了而已
# 数据优先填充X轴向，其次Y轴，其次Z轴
# ndarray的实现，就是C中的多维数组
