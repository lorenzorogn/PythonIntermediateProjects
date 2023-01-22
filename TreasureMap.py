row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

a = position.split()

b = int(a[0]) - 1
c = int(a[1]) - 1

map[c][b] = "X"

print(f"{row1}\n{row2}\n{row3}")

# lei lo fa senza mettere uno spazio tra i numeri quindi senza dover splittare
# i numeri in 2 valori nella lista 
