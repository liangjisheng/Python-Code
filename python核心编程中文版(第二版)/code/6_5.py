
print(type('xyz'));
# 在python中，圆括号被重载了，它也被用作分组操作符。由圆括号包含的一个单一
# 元素首先作为分组操作，而不是作为元组的分界符。可以在第一个元素后面添加一个
# 逗号，来表明这是一个元素，而不是在做分组操作
print(type(('xyz',)));

person = ['name', ['savings', 100]];
# 字符串为不可变对象，在进行浅拷贝时，字符串被显示的拷贝，并新创建了一个
# 字符串对象，而列表元素只是把它的引用赋值了一下，并不是它的成员
hubby = person[:];		# slice copy
wifey = list(person);	# fac func copy

print(person);
print(hubby);
print(wifey);
print([id(x) for x in (person, hubby, wifey)]);
print([id(x) for x in person]);
print([id(x) for x in hubby]);
print([id(x) for x in wifey]);

hubby[0] = 'joe';
wifey[0] = 'jane';
print(hubby);
print(wifey);
print([id(x) for x in person]);
print([id(x) for x in hubby]);
print([id(x) for x in wifey]);

hubby[1][1] = 50;	# wifey[1][1]也变成了50，原因是在创建的时候仅仅是做了浅拷贝
print(hubby);
print(wifey);
print();

# 使用深拷贝来创建新对象
person1 = ['name', ['savings', 100]];
hubby1 = person1;

# 包含两个函数:copy()进行浅拷贝，deepcopy()进行深拷贝
import copy;
wifey1 = copy.deepcopy(person1);
print([id(x) for x in (person1, hubby1, wifey1)]);

hubby1[0] = 'joe';
wifey1[0] = 'jane';
print(person1);
print(hubby1);
print(wifey1);

hubby1[1][1] = 50;
print(person1);
print(hubby1);
print(wifey1);

print([id(x) for x in hubby1]);
print([id(x) for x in wifey1]);
print();

# 1.非容器类型(比如数字，字符串和其他原子类型的对象)没有被拷贝一说，浅拷贝
# 是用完全切片操作来完成的。2.如果元组变量只包含原子类型对象，对它的深拷贝
# 将不会进行
person2 = ['name', ('savings', 100)];
newPerson2 = copy.deepcopy(person2);
print([id(x) for x in (person2, newPerson2)]);
print([id(x) for x in person2]);
print([id(x) for x in newPerson2]);