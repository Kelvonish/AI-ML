import pandas as pd
#data = {'name':['Tom','Bob','Ann'],'Age':[12,10,5]}
data_file = 'sample.csv'
cols=['First name','Last name','Age','County']
df=pd.read_csv(data_file,names=cols)
#df = pd.DataFrame(data)
sublist = df[['First name','Last name']]
few_rows = df[4:]
#print(df.loc[0:3,['First name', 'Last name']])
print(df.iloc[0:3,0:2])
#print(few_rows)
