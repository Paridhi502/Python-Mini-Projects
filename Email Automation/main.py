import smtplib
import datetime as dt
import random
my_email="rubybell354@gmail.com"
password="hvyd svwz hhmj vjgj"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email, to_addrs="tedbaker354@gmail.com", msg="Hello, Paridhi Kumar!!")
# connection.close()

import datetime as dt
now=dt.datetime.now()
weekday=now.weekday()
if weekday==0:
    with open('quotes.txt') as quote_file:
        all_quotes=quote_file.readlines()
        choice=random.choice(all_quotes)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Drive Away The Monday Blues\n\n{choice}")
    connection.close()


