import pandas as pd
from datetime import datetime
from datetime import timedelta
import datetime

df = pd.read_csv("timesheet.csv")
# df = pd.read_excel("timesheet.xlsx")
# today = datetime.now().date().strftime("%Y-%m-%d")
def last_day_of_month(year, month):
    return datetime.date(year, month + 1, 1) - datetime.timedelta (days = 1)
print(last_day_of_month(2018,10))
# print(df)
#
# print(df.loc[0,'In'])
# print(df.loc[0,'Out'])
# Out = datetime.strptime(df.loc[1]['Out'], '%Y-%m-%d %H:%M:%S.%f')
# In = datetime.strptime(df.loc[1]['In'], '%Y-%m-%d %H:%M:%S.%f')
# print(round((Out - In).total_seconds() / 3600, 2))

# df.to_csv("timesheet.csv", sep=',', index=False, encoding='utf-8')
