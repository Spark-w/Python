#列表脚本操作符
#列表截取
L=['Google','Runoob','Taobao']
print(L[2])
print(L[-2])
print(L[1:])
#Python列表函数和方法
list=[1,2,3]
list.append(4)
print(list)
print("------------------")
['to','be','or','not','to','be'].count('to')
print('---------------------------')
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

a=[1,2,3]#这里不是一个原位置操作
b=[4,5,6]
a+b
print(a+b)
print(a)

a=[1,2,3]
a.pop()
print(a)
print("---------------------")
a=[1,2,3]
a.append(a.pop())
print(a)
print("-------------------------")
a=[1,2,3,1,4,5,6]
a.remove(6)#移除列表中某元素且为第一个出现的元素
print(a)
print('----------------')
a=[1,2,3,4,5,6]
a.reverse()
print(a)
print("-------------------")
a=[4,6,2,1,7,9]
a.sort()
print(a)
print("---------------")
a=[4,6,2,1,7,9]
b=a[:]####################
b.sort()
print(a)
print(b)
