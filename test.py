import pandas as pd

df = pd.read_excel("timesheet.xlsx")

print(df)

print(df.loc[0,'In'])
print(df.loc[0,'Out'])

print(df.loc[0,'Out'] - df.loc[0,'In'])
