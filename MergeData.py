import pandas as pd

df = pd.read_csv('Data.csv',index_col=False)

for i in range(2013,2016,1):
    df1 = pd.read_csv(str(i)+'.csv',index_col=False)
    df = df.append(df1)
df.to_csv('Data.csv')