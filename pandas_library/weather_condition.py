# with open ("./weather_condition/weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open("./weather_condition/weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("./pandas_library/weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(data["temp"].max())

# print(data.condition)

# get data in row

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# create dataframe from scratch 

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("New_data.csv")
