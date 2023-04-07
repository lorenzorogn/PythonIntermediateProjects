import pandas as pd

data = pd.read_csv("./pandas_library/squirrel_data.csv")
squirrel_grey = len(data[data["Primary Fur Color"] == "Gray"])
squirrel_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
squirrel_black = len(data[data["Primary Fur Color"] == "Black"])


squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [squirrel_grey, squirrel_cinnamon, squirrel_black]
}


new_data = pd.DataFrame(squirrel_dict)
new_data.to_csv("./pandas_library/squirrel_color.csv")