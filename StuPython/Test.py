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
#print(Ttuple[-1])