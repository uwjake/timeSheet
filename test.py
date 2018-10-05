import pandas as pd
from datetime import datetime

df = pd.read_csv("timesheet.csv")
# df = pd.read_excel("timesheet.xlsx")


print(df)

print(df.loc[0,'In'])
print(df.loc[0,'Out'])
Out = datetime.strptime(df.loc[1]['Out'], '%Y-%m-%d %H:%M:%S.%f')
In = datetime.strptime(df.loc[1]['In'], '%Y-%m-%d %H:%M:%S.%f')
print(round((Out - In).total_seconds() / 3600, 2))

# df.to_csv("timesheet.csv", sep=',', index=False, encoding='utf-8')
