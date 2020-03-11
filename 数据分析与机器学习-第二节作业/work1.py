#1.S&P500股票在2015年net income的均值是多少？最大值比最小值多多少？
import pandas as pd
df = pd.read_csv('fundamentals.csv')
df['Period Ending'] = pd.to_datetime(df['Period Ending']) #将数据类型转换为日期类型
df = df.set_index('Period Ending') # 将date设置为index
df_2015 = df['2015']
net_income_mean = df_2015['Net Income'].mean()
max_min = df_2015['Net Income'].max()-df_2015['Net Income'].min()
print(f'S&P500股票在2015年net income的均值是{mean},最大值比最小值多{max_min}')

#S&P500股票在2016年的固定资产（fixed assets）占总资产(total assets)比例的均值是多少？固定资产占总资产比例最小的股票是的代码（ticker symbol）是什么？
df_2016 = df['2016']
def func(a, b):
    return a / b
df_2016['values'] = df_2016.apply(lambda x: func(x['Fixed Assets'],x['Total Assets']),axis=1)
df_2016_mean = df_2016['values'].mean()
df_2016 = df_2016[df_2016['values']!=0]
df_2016_min = df_2016[df_2016['values']==df_2016['values'].min()]
ticker_symbol = df_2016_min.iloc[0]['Ticker Symbol']
print(f'S&P500股票在2016年的固定资产（fixed assets）占总资产(total assets)比例的均值是{df_2016_mean},固定资产占总资产比例最小的股票是的代码（ticker symbol）是{ticker_symbol}')
