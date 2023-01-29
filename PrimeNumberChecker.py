# trovare i numeri primi

# mia versione
# def prime_checker(number):
#     if number % 2 == 0 and number != 2:
#         print("It's not a prime number.")
#     elif number % 3 == 0 and number != 3:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")

# sua versione
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)


