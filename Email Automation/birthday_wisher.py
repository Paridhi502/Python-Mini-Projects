import smtplib
import datetime as dt
import random

my_email = "rubybell354@gmail.com"
password = "hvyd svwz hhmj vjgj"

now = dt.datetime.now()
date_org = now.day
month_org = now.month

with open('birthdays.csv') as check:
    lines = check.readlines()
    for entry in lines:
        fields = entry.strip().split(',')
        name = fields[0]
        email_id = fields[1]
        month = int(fields[2])
        day = int(fields[3])
        if month == month_org and day == date_org:
            letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
            mail = random.choice(letters)
            with open(mail) as letter:
                content = letter.read()
                personalized_content = content.replace("[NAME]", name)

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email_id,
                    msg=f"Subject: Happiest Birthday!\n\n{personalized_content}"
                )
