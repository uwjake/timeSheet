import pandas as pd

df = pd.read_excel("timesheet.xlsx")

print(df)

print(df.loc[0,'In'])
print(df.loc[0,'Out'])

print(round((df.loc[1]['Out'] - df.loc[1]['In']).total_seconds() / 3600, 2))
