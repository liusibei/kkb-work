#第一步：读取样本数据，并将数据集分为训练集和测试集

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv('data(1).csv')
x = data.iloc[:,0:4]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.3,random_state =12345)

#第二步：训练Linear Regreesion模型，得到训练参数

lr = LinearRegression()
lr.fit(x_train,y_train)
print(lr.coef_)
print(lr.intercept_)

#第三步：使用均方误差和均方根误差在测试集上的表现来评价模型的好坏。

y_test_pred = lr.predict(x_test)
MSE = metrics.mean_squared_error(y_test,y_test_pred)
RMSE = np.sqrt(MSE)
print('MSE:'+str(MSE))
print('RMSE:'+str(RMSE))

#第四步：可视化的方式直观的表示模型学习效果的好坏

plt.scatter(y_test,y_test_pred,color = 'y',marker = 'o')
plt.scatter(y_test,y_test,color = 'g',marker = '+')
