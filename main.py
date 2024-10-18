import random
import smtplib
import datetime as dt

MY_EMAIL ="divithtest@gmail.com"
MY_PASSWORD ="wgpf xshy ylzf qbzh"

now = dt.datetime.now()
weekday = now.weekday()
if weekday ==0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg= f"Subject: Monday Motivation \n\n {random_quote}")