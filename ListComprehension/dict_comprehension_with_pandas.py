import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# looping through dictionaries:

"""for (key,value) in student_dict.items():
    print(value)"""


student_data_frame = pd.DataFrame(student_dict)


# loop through a data frame

"""for (key,value) in student_data_frame.items():
    print(value)"""

# loop through rows of a data frame

for (index,row) in student_data_frame.iterrows():
    # print(row.student)
    if row.student == "Angela":
        print(row.score)

