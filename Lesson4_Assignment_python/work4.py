#方法一
#导入模块
import numpy as np
#生成数组
x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']
arr=np.array([x,y]).T
#打乱索引
index = [i for i in range(len(arr))] 
np.random.shuffle(index) 
arr1=arr[index]
#打印结果
for i in arr1:
    print(f'{i[0]}:{i[1]}')

#方法二
from random import randint

def shuffle(x,y):
    for i in range(10):
        index1 = randint(0,len(x)-1)
        index2 = randint(0,len(x)-1)
        x[index1],x[index2] = x[index2],x[index1]
        y[index1],y[index2] = y[index2],y[index1]
    return x,y

x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']
x,y = shuffle(x,y)

for i,j in zip(x,y):
    print(f'{i}:{j}')
    
#方法三（想用集合的无序性打乱，测试后发现，集合的无序性也只有一种排列方式，只能打乱成一种固定的顺序）
x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']
x_y = dict(set(zip(x,y)))
for k,v in x_y.items():
    print(f'{k}:{v}')
