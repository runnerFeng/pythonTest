#coding=utf-8

# 1.输出单个字符串
# print('\n--------1------------')
# print('hello world')

# 2.输出多个字符串
# print('\n--------2------------')
# print('hello','august')
# 2.1 \转义
# print('i\'m ok')
# print('i\'m "ok"')
# print('i\'m \"ok\"')
# 2.2 r''标识''内部的字符无需转义
# print(r'i\'m ok')
# 2.3 \n换行
# print('the lesson we can \n learn from chuck and all the others...')
# 2.4 '''开头结尾标识多行
# print('''line1
# line2
# line3''')
# 2.5 '''开头结尾前加上r标识内部字符无需转义
# print(r'''line4\x
# line5''')

# 3.输出整数
# print('\n--------3------------')
# print(300)

# 4.计算
# print('\n--------4------------')
# print(200+100)
# print('200+100=',200+100)

# 5.input()函数输入
# print('\n--------5------------')
#name = input("please enter your name:")
#print('hello',name)

# 6.布尔值:True,False
# 6.1
# print('\n--------6------------')
# print(True)
# print(False)
# print(3>2)
# 6.2. 布尔值可以和and,or,not一起运算
# print(not True)

# 7.空值:None
# print('\n--------7------------')
# print(None)

# 8.除法:/,//
# 8.1:/的结果任然是浮点数，即使是整数整除也是如此
# print('\n--------8------------')
# print(10/3)
# print(10/2)
# 8.3:/(地板除结果是整数，即使是结果有余数)
# print(10//3)

# 9.bytes类型的数据用d带b前缀的单引号或双引号表示
# print('\n--------9------------')
# print(b'xb')
# 9.1.英文str转bytes
# print('ABC'.encode('ascii'))
# 9.2.中文str转bytes,但是此时会报错，因为中文的编码范围超出了ascii的编码范围（如果bytes中只有一小部分
# 无效字节，可以用errors='ignore'忽略），此时要用UTF-8编码来处理
# print('浦东'.encode('ascii'))
# print('浦东tushuguan'.encode('ascii',errors='ignore'))
# print('浦东'.encode('UTF-8'))
# 9.3.计算str占用多少个字节用len()函数
# print(len('测试'))
# 9.4.计算bytes占用字节数
# print(len(b'pu'))
# print(len('浦东'.encode('UTF-8')))

# 10.字符串的格式化输出,用%连接占位符，单个占位符不用括号，多个需要用括号
# 10.1.同c语言 1:%s字符串 2:%d整数 3:%?占位符 4:%f浮点数
# print('\n-----------10-----------')
# print('hello,%s' % 'lux')
# print('hello,%s,i\'m jinx,i was %d years old' % ('lux',29))

# 10.2.如果字符串中包含%则可以用%%转义为%
# print('i\'m from %s,where are u from %% ',('GanSu'))

# 11.集合list
# print('\n-----------11-----------')
# classmate = ['fans','mu','ruguo']
# print(classmate)
# print(classmate[0])
# classmateLen = len(classmate)
# print(classmateLen)
# 11.1.获取集合中最后一个元素
# print(classmate[-1])
# print(classmate[classmateLen-1])
# 11.2.追加元素到末尾,类型可以不同
# classmate.append(67)
# print(classmate)
# 11.3.插入到指定位置
# classmate.insert(0,'dd')
# print(classmate)
# onePerson = classmate.pop()
# print(onePerson)
# 11.4.替换指定位置的元素
# classmate[1] = 'doctor';
# print(classmate)
# 11.5.集合中的某个元素也可以是其他集合，此时相当于一个二维数组
# anotherCollection = ['jack','alice']
# classmate.append(anotherCollection);
# print(classmate)
# print(classmate[4][1])

# 12.元组tuple:和list相似但是tuple一旦初始化就不能修改
# print('\n--------12------------')
# company = ("lf",'wx')
# print(company)
# print(company[0])
# 12.1.只有一个元素的tuple可以添加一个逗号来消除数学计算意义上的歧义
# company=(1)
# print(company)
# company=(1,)
# print(company)
# 12.2.其实tuple的不变指的是指向不变，类似于指向这个元素的指针不变，但是该元素是可以改变的
# company = ('x','y',['z','u'])
# print(company)
# company[2][1]='s'
# print(company)

# print('\n--------13------------')
# 13.条件判断
# age = 28
# if age>18:
#     print('adult')

# if age >18 :
#     print('adult')
# else:
#     print('teenage')

# age = 3
# if age > 18:
#     print('adult')
# elif age>6:
#     print('teenage')
# else :
#     print('kid')
# 13.1.if简写：只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False，如下
# x = 1
# if x:
#     print(True)

# print('\n--------14------------')
# 14.再议input:input返回str，如果输入的是int类型的数据，则需要int()函数进行转换
# b = input("please enter your birth:")
# print(b)
# birth = int(b)
# if birth > int(birth):
#     print('新时代青年')
# else:
#     print('老年人')

# print('\n--------15------------')
# 15.循环:python的循环有两种
# 15.1.for...in循环
# names = ['jinx','aug','leona']
# for name in names:
#     print(name)

# sum = 0;
# for x in [1,2,3,4,5,6,7,8]:
#     sum += x
# print(sum)

# 15.2.1-100等差数列求和：通过range()函数，可以生成一个整数序列，再通过list()函数生成一个list，然后求和
# s = 0
# coll = range(101)
# print(coll)
# for x in list(coll):
#     s+=x
# print(s)

# 15.3.第二种while循环:求1-100之间奇数之和
# sum = 0
# n = 99
# while n > 0:
#     sum +=n
#     n-=2
# print(sum)

# 15.4.求1-100之间的偶数之和
# sum = 0
# n = 100
# while n > 0:
#     sum += n
#     n -=2
# print(sum)

# print('\n--------15------------')
# 16.break:打印1-100
# n = 1
# while n < 100:
#     if n > 10:
#         break
#     print(n)
#     n+=1
# print('end')

# print('\n--------16------------')
# 16.continue:打印1-10的奇数
n =0 
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# print('\n--------17------------')
# 17.dict:字典,需要牢记的是dict的key必须是不可变对象，如字符串，整数等
d = {'jinx':98,'lux':97}
print(d['jinx'])

d['leona']=99
print(d)

# 17.1.判断字典中是否存在某个key的两种方法:in语句，get()方法
print('jinx' in d)
print(d.get('jin'))
# 17.2.删除一个key:pop()
d.pop('jinx')
print(d)

# 18.set
# print('\n--------18------------')
s = set([0,2,2,3])
print(s)
s.add(4)
print(s)
s.discard(5)
print(s)

# 18.1.set的交集，并集
s1= set([1,2,5])
t = s & s1
print(t)
print(s | s1)

# print('\n--------19------------')
# 19.函数:查询函数用法用help()函数，函数名其实是一个指向函数对象的引用，所以可以把函数名赋值给一个变量
# help(abs)
b = abs
print(b(-1))
# 19.1.定义函数：定义一个求绝对值的函数
# def my_abs (x):
#     if x>0:
#         return x
#     else:
#         return -x

# print(my_abs(-2))

# 19.2.引入定义好的函数
from abstest import my_abs
print(my_abs(-2))

# 19.2.定义一个空函数:可以使用pass语句，pass语句实际什么都不做，只是一个占位符
def todo_method():
    pass
print(todo_method())

def my_method(x):
    if x>2:
        pass
    else:
        print('param value less than 2')
my_method(1)

# 19.3.自定义函数的参数检查:isinstance()
# my_abs('1')

# 19.4.
import math
print(math.sin(30))
