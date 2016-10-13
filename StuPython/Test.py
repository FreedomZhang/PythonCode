classmates=['Michael','Bob','Tracy']
#len() 获取长度
#classmates[-1] 取最后一个索引值 类似[-2][-3]...
classmates.append('Adam') #追加元素到末尾
classmates.insert(1,'Jack')#把元素插入到指定位置 比如索引号为1的位置
classmates.pop()#删除末尾的元素
classmates.pop(1)#删除指定位置的元素pop(i)其中i是索引位置
classmates[1]='Sarah'#将索引为1的元素替换成Sarah
ListT=['Apple',123,True]#元素的数据类型可以不同
ListT2=['python','java',['asp','C#'],'php']#list元素可以是另一个list
#print(ListT2[2][0]) 获取第二个集合的第一个元素


#tuple 一种有序列表  tuple一旦初始化就不能修改 没有append(),insert()这样的方法其他事list是一样的可以用Ttuple[0],Ttuple[-1]
Ttuple=('Michael','Bob','Tracy')
Ttuple2=('A','B',['C','D'])
Ttuple2[2][0]='X'
Ttuple2[2][1]='Y'
#tuple的指向没有改变 但是Ttuple2中的list发生改变

'''
age=20
if age>=18:
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')
'''

#elif 是else if的缩写，可以有多个
#if语句执行从上往下判断,如果在某个判断上是True,把该判断对应的语句执行后，就忽略剩下的elif和else

#int()转换为int类型


'''
#for 循环
names=['Michael','Bob','Tracy']
for name in  names:
    print(name)

Lnum=list(range(5))#生成从0开始小于5的整数
#while循环
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
'''

#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
Dnames={'Michael':95,'Bob':75,'Tracy':85}
Dnames['Adam']=67#添加一个新的key-value
Dnames['Adam']=11#一个key只能对应一个value，多次对一个key放入value，后面的值会替换之前的value
#通过in判断key是否存在
Dt= 'Adam' in Dnames
#1.判断Adam是否存在 输出True
#通过dict提供的get方法，如果key不存在返回None，存在返回value  返回None的时候Python的交互式命令行不显示结果
Dt2=Dnames.get('Michael')#返回95 Dt2=Dnames.get('Michael1')返回None
#使用pop(key)方法删除key
Dnames.pop('Adam') #删除Adam
#dict内部存放的顺序和key放入的顺序是没有关系的
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
Sset=set([1,2,3])
#传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的
#Sset=set([1, 1, 2, 2, 3, 3])#输出{1, 2, 3}重复数据被过滤掉了
#通过add(key)方法添加元素到set中
Sset.add(4)
#通过remove(key)方法删除元素
Sset.remove(4)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
Sset1=set([1, 2, 3])
Sset2=set([2, 3, 4])
JL=Sset1&Sset2#交集
BJ=Sset1|Sset2#并集

print(BJ)