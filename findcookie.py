import argparse
import pandas as pd
import datetime
import re

my_parser = argparse.ArgumentParser(description='Find Most active cookie')
my_parser.add_argument('-f', action='store', type=str, required=True,help= "Enter the full path of the file; C:\cookie\cookies_log.csv")
my_parser.add_argument('-d', action='store', type=str, required=True,help= "Enter the date; 2018-12-09")

args = my_parser.parse_args()
argument_dict = dict(vars(args))
filename = argument_dict["f"]
date = argument_dict["d"]
if re.match('^\d{4}-\d{2}-\d{2}$',date) is None:
    print("Date format is not matching %Y-%m-%d(Eg. 2018-12-06)")
else:
    try:
        df = pd.read_csv(filename)
        df = df[df['timestamp'].str.contains(date)]
        duplicatecookie = df[df.duplicated(["cookie"])]
        if duplicatecookie.empty:
            if df.empty:
                print("Sorry! Dint find any cookie on the given date")
            else:
                print(df["cookie"].iloc[0])
        else:
            for cookie in duplicatecookie["cookie"].values.tolist():
                print(cookie)
        
    except Exception as e:
        print("make sure inputs are correct csv path & date")
        print("findcookie -h for the help")


