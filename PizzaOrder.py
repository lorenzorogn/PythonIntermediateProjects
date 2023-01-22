print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Doyou want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    else: pass
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    else: pass
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    else: pass

if extra_cheese == "Y":
    bill += 1
else: pass

print(f"Your final bill is: ${bill}.")
