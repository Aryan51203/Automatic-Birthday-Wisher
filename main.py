import datetime as dt
import smtplib
import random
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
your_name = os.getenv("YOUR_NAME")

today_date = dt.datetime.now()


def send_email(name, recv_addr):
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()

        conn.login(user=my_email, password=my_password)

        ind = random.randint(1, 3)

        msg = "Subject:Happy Birthday\n\n"

        with open(f"./letter_templates/letter_{ind}.txt") as file:
            text_ind = (
                file.read().replace("[NAME]", name).replace("[YOUR_NAME]", your_name)
            )
            msg += text_ind

        conn.sendmail(from_addr=my_email, to_addrs=recv_addr, msg=msg)


with open("birthdays.csv") as file:
    l = file.readlines()

    for i in range(1, len(l)):
        m = l[i].strip().split(",")
        if m[3] == str(today_date.month) and m[4] == str(today_date.day):
            print("Sending email")
            send_email(m[0], m[1])
