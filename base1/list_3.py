
# 演示列表的一些操作

# list.count(x)返回元素x在列表中的个数
a = [66.25, 333, 333, 1, 1234.5];
print(a.count(333), a.count(66.25), a.count("x"));

# 在索引2处的位置插入-1这个值
a.insert(2, -1);
# 追歼
a.append(333);
print(a);

# list.index(x)返回元素x在列表中第一次出现的索引
print(a.index(333));

# 删除第一个为333的元素值的元素
a.remove(333);
print(a);

# 反转
a.reverse();
print(a);

a.sort();
print(a);
print();


# 列表方法使得列表可以很方便的作为一个堆栈来使用
stack = [3, 4, 5];
stack.append(6);
stack.append(7);
print(stack);

stack.pop();
print(stack);

stack.pop();
stack.pop();
print(stack);

# 将列表当做队列使用
from collections import deque;
queue = deque(["Eric", "John", "Michael"]);
print(queue);
queue.append("Terry");
queue.append("Graham");
print(queue);

print(queue.popleft());
print(queue.popleft());
print(queue);


input();