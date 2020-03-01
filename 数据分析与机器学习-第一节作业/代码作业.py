import math

def func_knn(c,k=1):
    datalist = [[1,1,2],
                [0.4,5.2,1],
                [-2.8,-1.1,2],
                [3.2,1.4,1],
                [-1.3,3.2,1],
                [-3,3.1,2]]
    distance = list()
    for i in range(0,len(datalist)):
        d = math.sqrt((datalist[i][0]-c[0])**2+(datalist[i][1]-c[1])**2)
        datalist[i].append(d)
        distance.append(d)
    distance.sort()
    distance_k = distance[:k]
    label = []
    for i in distance_k:
        for v in datalist:
            if i == v[3]:
                label.append(v[2])
    
    label_1 = label.count(1)
    label_2 = label.count(2)
    if label_1 > label_2:
        print(f'{c}分类标签为1')
    elif label_1 < label_2:
        print(f'{c}分类标签为2')
    else:
        print(f'{c}无法判断')
        
func_knn((-2.6,6.6))
func_knn((1.4,1.6))
func_knn((-2.5,1.2))
