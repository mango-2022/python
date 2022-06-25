import csv
import pandas

with open('./weather_data.csv') as weather_data:
    data = weather_data.readlines()
    print(data)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] != 'temp':
            new_temp = int(row[1])
            temperatures.append(new_temp)

    print(temperatures)

data = pandas.read_csv('weather_data.csv')
print(data['temp'])

# DataFrame
data_dict = data.to_dict()
temp_list = data['temp'].to_list()
average_temp = data['temp'].mean()

# attribute
data.condition

# get data in rows / Series
data[data.temp == data.temp.max()]
monday = data[data.day == 'Monday']
monday.condition  # get cell

# create a data frame from scratch
data_dict = {
    'students': ['Amy', 'Sam', 'Angela'],
    'score': [76, 58, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")  # create a new file

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("primary_fur_color_count.csv")
