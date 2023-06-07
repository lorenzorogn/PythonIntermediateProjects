"""file not found"""
# file = open("Error_Exception_JSONData/a_file.txt")


"""key error"""
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]


"""index error"""
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]


"""type error"""
# text = "abc"
# print(text + 5)


# try:
#     file = open("Error_Exception_JSONData/a_file.txt")
#     a_dictionary = {"key":"value"}
#     value = a_dictionary["non_existent_key"]
# except FileNotFoundError:
#     print("FileNotFoundError")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     print("stampo comunque")
    
    

# posso usare un raise error per farmi tornare un'errore
# qualunque io voglia

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)


# esercizio 1

# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + "pie")

# make_pie(4)




# esercizio 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         pass

# print(total_likes)



