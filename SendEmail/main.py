# import smtplib

# my_email = "testpythoncorso@gmail.com"
# password = "francesco10!"
  
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="testpythoncorso@yahoo.com", 
#         msg="Subject:bella pe te\n\nThis is the body of my email"
#     )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# print(day_of_the_week)
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)


import smtplib
import datetime as dt
from random import *

my_email ="testpythoncorso@gmail.com"
password = "francesco10!"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("SendEmail\quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = choice(all_quote)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )