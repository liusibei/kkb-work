print('''1. 请思考，合并两个表的信息的时候，我们应该用什么样的准则对其它们（10分）
以两个表的共有数据为准进行合并。
两个表一个是股票的年报数据，一个是股票的基本信息，所以两个表的共有数据就是股票名称。重要的是股票的年报数据，所以是将股票的基本信息添加到股票的年报数据表里。
使用merge合并数据，但是两个表columns的股票名称略有差异，所以要先将两个表的股票名称统一后，再将股票的基本信息这张表按照股票名称使用merge合并到股票的年报数据表里''')
print('*'*100)

#2. 请列举每个sector在2013-2016年累计Research&Development的总投入（10分）
import pandas as pd
df1 = pd.read_csv('fundamentals.csv')
df2 = pd.read_csv('securities.csv')
df2.rename(columns={'Ticker symbol':'Ticker Symbol'}, inplace = True)
df = df1.merge(df2,on='Ticker Symbol')
df['Period Ending'] = pd.to_datetime(df['Period Ending']) 
df_2013_2016 = df[(df['Period Ending']>='2013')&(df['Period Ending']<'2017')]
sector_sum = df_2013_2016.groupby(df['GICS Sector'])['Research and Development'].sum().astype('int64')
for i in range(sector_sum.shape[0]):
    sector=sector_sum.index[i]
    RD_sum=sector_sum[i]
    print(f'{sector}在2013-2016年累计Research&Development的总投入为{RD_sum}')
    
#3. 请列举出每个sector中，在2013-2016年累计Research&development投入最大的3家公司的名称以及投入的数值（20分）
