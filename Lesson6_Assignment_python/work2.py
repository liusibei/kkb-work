import pandas as pd

dataset = \
"""编号 色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
1 青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
2 乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
3 乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
4 青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
5 浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
6 青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
7 乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
8 乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
9 乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
10 青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
11 浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
12 浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
13 青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
14 浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
15 乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
16 浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
17 青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""

dataset1 = dataset.replace(' ',',')
# 将数据写入csv文件
with open('D:\machine_learning.csv','w') as f:
    f.write(dataset1)
print('csv file is generated!') 
file = r'D:\machine_learning.csv' # 文件名称，学员可修改或不修改

# 向csv文件中加入一条新的数据（数据已给出）
inser_data = '18 青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 是'
inser_data1 = '\n'+inser_data.replace(' ',',')+'\n'
with open(file,'a') as f:
    f.write(inser_data1)
print('csv file is generated!')

# 查看全体数据
df = pd.read_csv(file,encoding='gbk')
print(df.head(20))

# 读取文件存储的数据
columns = []
datalist = []

with open(file,'r') as f:
    for i in f.readlines():
        k= i.replace('\n','')
        datalist.append(k.split(','))
    columns = datalist[0]
    
# 验证数据信息是否相符
print(columns==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1]==['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '是'])
        
    
# 在所有数据中过滤出色泽='浅白'的数据
with open(file,'a') as f:
    f.write("\n")
def func(x):
    s = ','.join(x)+'\n'
    return s
QB = list(filter(lambda x:'浅白'in x,datalist))
QB1 = list(map(func,QB))
for i in QB1:
    if i==None:
        pass
    else:
        with open(file,'a') as f:
            f.write(i)
print('csv file is generated!')

# 在所有数据中过滤出密度大于0.5的数据
with open(file,'a') as f:
    f.write("\n")
MD = list(filter(lambda x:False if x[7]=='密度' else float(x[7])>0.5,datalist))
MD1 = list(map(func,MD))
for i in MD1:
    if i==None:
        pass
    else:
        with open(file,'a') as f:
            f.write(i)
print('csv file is generated!')

# 查看全体数据
df = pd.read_csv(file,encoding='gbk')
print(df.head(35))
