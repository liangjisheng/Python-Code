
# 多重继承

class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
		
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
		
# 另一个类
class speaker():
	topic = "";
	name = "";
	def __init__(self, n, t):
		self.name = n;
		self.topic = t;
	def speak(self):
		print("我叫 %s, 我是一个演说家，我演讲的主题是 %s" %(self.name, self.topic));
		
class sample(speaker, student):
	a = "";
	def __init__(self, n, a, w, g, t):
		speaker.__init__(self, n, t);
		student.__init__(self, n, a, w, g);

test = sample("Tim", 25, 80, 4, "python");
# 方法名相同，默认调用的是在括号中排前的父类的方法
test.speak();