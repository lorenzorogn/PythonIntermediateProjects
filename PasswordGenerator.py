import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# easy level secondo me 
# letter = random.choices(letters, k=nr_letters)
# # print(letter)
# symbol = random.choices(symbols, k=nr_symbols)
# # print(symbol)
# number = random.choices(numbers, k=nr_numbers)
# # print(number)
# password = letter+symbol+number
# print("".join(password)) #.join mi unisce le varie liste in una sola stringa

# easy level secondo lei
# password = ""
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
#     # versione short password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# hard level

password = []

for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

print(password)
random.shuffle(password)
print(password)

random_pass = ""
for char in password:
    random_pass += char

print(f"Your password is: {random_pass}")

