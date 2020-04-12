import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('data(1).csv')
x = data.iloc[:,:-1]
y = data.iloc[:,-1:]

#数据预处理
sc = StandardScaler()
x_pred = sc.fit_transform(x)

#添加偏置
def add_ones(x):
    ones = np.ones((x.shape[0],1))
    x = np.hstack((ones,x))
    return x
x_pred = add_ones(x_pred)

#划分数据集
x_train,x_test,y_train,y_test = train_test_split(x_pred,y,test_size=0.3,random_state=123)

#SVR
svr = SVR()
svr.fit(x_train,y_train)
svr_score = svr.score(x_test,y_test)
print("SVR score:",svr_score)

#决策树
dr = tree.DecisionTreeRegressor()
dr.fit(x_train,y_train)
dr_score = dr.score(x_test,y_test)
print("DecisionTree score:",dr_score)
