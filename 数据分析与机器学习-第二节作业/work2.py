#1.请列举出各个sector中的加入时间最早的股票名称
import pandas as pd
df = pd.read_csv('securities.csv')
df = df[df['Date first added']<'NaN']
df['Date first added'] = pd.to_datetime(df['Date first added'])
df_min = df.groupby(df['GICS Sector'])[['Date first added']].min()
for i in range(df_min.shape[0]):
    df1=df[(df['GICS Sector']==df_min.index[i])&(df['Date first added']==df_min.iloc[i]['Date first added'])]
    GICS_Sector = df1.iloc[0]['GICS Sector']
    Ticker_symbol = df1.iloc[0]['Ticker symbol']
    print(f'{GICS_Sector}加入时间最早的股票名称为{Ticker_symbol}')   

print('*'*100)

#2.请列举出每一个州中加入时间最晚的股票名称
df_max = df.groupby(df['Address of Headquarters'])[['Date first added']].max()
for i in range(df_max.shape[0]):
    df1=df[(df['Address of Headquarters']==df_max.index[i])&(df['Date first added']==df_max.iloc[i]['Date first added'])]
    Address = df1.iloc[0]['Address of Headquarters']
    Ticker_symbol = df1.iloc[0]['Ticker symbol']
    print(f'{Address}加入时间最晚的股票名称为{Ticker_symbol}')
