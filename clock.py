import sys
from datetime import datetime
from datetime import timedelta
import pandas as pd

time_now = datetime.now()
today_date = time_now.date()
time_now

def last_day_of_month(year, month):
    return datetime.date (year, month+1, 1) - datetime.timedelta (days = 1)

def save(df):
    # writer = pd.ExcelWriter('timesheet.xlsx')
    # writer.save()
    df.to_csv("timesheet.csv", sep=',', index=False, encoding='utf-8')
    print(df.head())

def clock_in():
    df = pd.read_csv("timesheet.csv")
    print(df)
    df.loc[-1] = [today_date, time_now, 0.0, 0.0]  # adding a row
    df.index = df.index + 1  # shifting index
    df.sort_index(inplace=True)
    return df

def read_strptime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')

def clock_out():
    df = pd.read_csv("timesheet.csv")
    df.at[0,'Out'] = time_now
    # Out = read_strptime(df.loc[0]['Out'])
    In = read_strptime(df.loc[0]['In'])

    df.loc[0,'Hour'] = round((time_now - In).total_seconds() / 3600, 1)
    if len(df[df["Date"] == today_date.strftime("%Y-%m-%d")]) > 1:
        print('Multiple entry for today')
        print('*'*40)

        return df
    else:
        return df

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        if sys.argv[1] == "in":
            type = "1"
        elif sys.argv[1] == "out":
            type = "2"
        else:
            type = "0"
    else:
        type = input('1 for clock in, 2 for clock out: \n')
        
    print('*'*40)
    if (type == "1"):
        save(clock_in())
        print("Clocked in!")
    elif (type == "2"):
        save(clock_out())
        print("Clocked out!")
    else:
        print("What are you talking about?")
        print('*'*40)
