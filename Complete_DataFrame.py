import pandas as pd


pd.set_option('display.max_rows', 150)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 5000)


names_2016 = ["ID", "Date,Time", "E", "N", "Outcome", "Type", "Description"]
my_dataFrame_2016 = pd.read_excel("SaobracajBeograd2016.xls",  header = None, names = names_2016)

my_dataFrame_2016["E"] = my_dataFrame_2016["E"].str.replace(",", ".")
my_dataFrame_2016["N"] = my_dataFrame_2016["N"].str.replace(",", ".")
my_dataFrame_2016[["E", "N"]] = my_dataFrame_2016[["E", "N"]].astype(float)


names_2017 = ["ID", "Date,Time", "E", "N", "Outcome", "Type", "Description"]
my_dataFrame_2017 = pd.read_excel("SaobracajBeograd2017.xls",  header = None, names = names_2017)

names_2018 = ["ID", "Date,Time", "E", "N", "Outcome", "Type", "Description"]
my_dataFrame_2018 = pd.read_excel("SaobracajBeograd2018.xls",  header = None, names = names_2018)

names_2019 = ["ID", "Date,Time", "E", "N", "Outcome", "Type", "Description"]
my_dataFrame_2019 = pd.read_excel("SaobracajBeograd2019.xls",  header = None, names = names_2019)


my_dataFrame = pd.concat([my_dataFrame_2016, my_dataFrame_2017, my_dataFrame_2018, my_dataFrame_2019])
