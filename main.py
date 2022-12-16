# with open("weather_data.csv") as weatherdata:
#     data = weatherdata.readlines()
#
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature =[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#

# import pandas
# data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
# new_data = data.to_dict()
# print(new_data)
# print(new_data["day"][0])
#
#get data in column
#print(data["temp"])
#convert to list
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

#get data in row
# print(data[data.temp == data.temp.max()])
#
# maxtemp_row = data[data.temp == data.temp.max()]
# print(maxtemp_row.temp*(9/5)+32)
#
# #creating a dataframe from scratch
# data_dict = {
#     "students":["a","b","c"],
#     "scores":[23,65,45]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# #we can convert this dataframe to csv file and it gets stored in a new file
# data.to_csv("new_data.csv")

import pandas
squi_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_Gray = squi_data[squi_data["Primary Fur Color"] == "Gray"]
data_Black = squi_data[squi_data["Primary Fur Color"] == "Black"]
data_Cinnamon = squi_data[squi_data["Primary Fur Color"] == "Cinnamon"]
new_data = {
"primary Fur Color":["Gray","Black","Cinnamon"] ,
"count of squirrels":
[data_Gray["Primary Fur Color"].count(),
data_Black["Primary Fur Color"].count(),
data_Cinnamon["Primary Fur Color"].count()]
}
squirrels_by_color=pandas.DataFrame(new_data)
#print(squirrels_by_color)
squirrels_by_color.to_csv("squirrels_by_color.csv")
