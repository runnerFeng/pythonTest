#coding=utf-8

# 1.输出单个字符串
print('\n--------1------------')
print('hello world')

# 2.输出多个字符串
print('\n--------2------------')
print('hello','august')
# 2.1 \转义
print('i\'m ok')
print('i\'m "ok"')
print('i\'m \"ok\"')
# 2.2 r''标识''内部的字符无需转义
print(r'i\'m ok')
# 2.3 \n换行
print('the lesson we can \n learn from chuck and all the others...')
# 2.4 '''开头结尾标识多行
print('''line1
line2
line3''')
# 2.5 '''开头结尾前加上r标识内部字符无需转义
print(r'''line4\x
line5''')

# 3.输出整数
print('\n--------3------------')
print(300)

# 4.计算
print('\n--------4------------')
print(200+100)
print('200+100=',200+100)

# 5.input()函数输入
print('\n--------5------------')
#name = input("please enter your name:")
#print('hello',name)

# 6.布尔值:True,False
# 6.1
print('\n--------6------------')
print(True)
print(False)
print(3>2)
# 6.2. 布尔值可以和and,or,not一起运算
print(not True)

# 7.空值:None
print('\n--------7------------')
print(None)

# 8.除法:/,//
# 8.1:/的结果任然是浮点数，即使是整数整除也是如此
print('\n--------8------------')
print(10/3)
print(10/2)
# 8.3:/(地板除结果是整数，即使是结果有余数)
print(10//3)

# 9.bytes类型的数据用d带b前缀的单引号或双引号表示
print('\n--------9------------')
print(b'xb')
# 9.1.英文str转bytes
print('ABC'.encode('ascii'))
# 9.2.中文str转bytes,但是此时会报错，因为中文的编码范围超出了ascii的编码范围（如果bytes中只有一小部分
# 无效字节，可以用errors='ignore'忽略），此时要用UTF-8编码来处理
# print('浦东'.encode('ascii'))
print('浦东tushuguan'.encode('ascii',errors='ignore'))
print('浦东'.encode('UTF-8'))
# 9.3.计算str占用多少个字节用len()函数
print(len('测试'))
# 9.4.计算bytes占用字节数
print(len(b'pu'))
print(len('浦东'.encode('UTF-8')))

# 10.字符串的格式化输出,用%连接占位符，单个占位符不用括号，多个需要用括号
# 10.1.同c语言 1:%s字符串 2:%d整数 3:%?占位符 4:%f浮点数
print('\n-----------10-----------')
print('hello,%s' % 'lux')
print('hello,%s,i\'m jinx,i was %d years old' % ('lux',29))

# 10.2.如果字符串中包含%则可以用%%转义为%
print('i\'m from %s,where are u from %% ',('GanSu'))

# 11.集合list
print('\n-----------11-----------')
classmate = ['fans','mu','ruguo']
print(classmate)
print(classmate[0])
classmateLen = len(classmate)
print(classmateLen)
# 11.1.获取集合中最后一个元素
print(classmate[-1])
print(classmate[classmateLen-1])
# 11.2.追加元素到末尾,类型可以不同
classmate.append(67)
print(classmate)
# 11.3.插入到指定位置
classmate.insert(0,'dd')
print(classmate)
onePerson = classmate.pop()
print(onePerson)
# 11.4.替换指定位置的元素
classmate[1] = 'doctor';
print(classmate)
# 11.5.集合中的某个元素也可以是其他集合，此时相当于一个二维数组
anotherCollection = ['jack','alice']
classmate.append(anotherCollection);
print(classmate)
print(classmate[4][1])

# 12.元组tuple
print('\n--------12------------')
