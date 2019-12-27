#In the future when I run the script I'd like to export a CSV of all transactions from the month.

#Date range: (complete)
#Sum of outgoing: (complete)
#Sum of incoming: (complete)
#Net for the time period: (complete)
#Total Balance: (complete)

#present it somewhere.

import pandas as pd

df = pd.read_csv('../Data/Chase6289_Activity_20191223.CSV')

Start = df.iloc[:,0].tail(1).sum()
End = df.iloc[:,0].head(1).sum() 
Income = df.iloc[:,2].where(df.iloc[:,2]>0).dropna().sum()
Outflow = df.iloc[:,2:].where(df.iloc[:,2:]<0).sum(axis=1).sum()
Net = Income + Outflow
Balance = df.iloc[0,4]

print ("Start Date", Start)
print ("End Date", End)
print ("Income for time period", Income)
print ("Outflow for time period", Outflow)
print ("Net for time period", Net)
print ("Current Balance", Balance)
