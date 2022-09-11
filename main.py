
import random, datetime as dt, smtplib, pandas
import os
from dotenv import load_dotenv
load_dotenv()

gmail = os.getenv('GMAIL')
g_password = os.getenv('G_PASSWORD')
y_password = os.getenv('Y_PASSWORD')
yahoomail = os.getenv('YAHOOMAIL')
g_port = 587
g_host = "smtp.gmail.com"

PLACEHOLDER= "[NAME]"
letters = ["letter_templates\letter_1.txt", "letter_templates\letter_2.txt", "letter_templates\letter_3.txt"]
letter = random.choice(letters)

now = dt.datetime.now()
day = now.day
month = now.month

birthday_df = pandas.read_csv("birthdays.csv")

for (index,birthday) in birthday_df.iterrows():
    b_day = birthday.day
    b_month = birthday.month
    b_name = birthday["name"]

    if day == b_day and month == b_month:
        with open(letter,"r") as file:
            lines = file.read()
            header = lines.replace(PLACEHOLDER,b_name)

        with smtplib.SMTP(host=g_host,port=g_port) as connection:
            connection.starttls()
            connection.login(user=gmail,password=g_password)
            connection.sendmail(
                from_addr=gmail,
                to_addrs= birthday["email"],
                msg= header
            )

# today = dt.datetime.now()
# today_tuple = (today.month,today.day)
#
# data = pandas.read_csv("birthdays.csv")
#
# birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}
#
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#     with smtplib.SMTP(host=g_host, port=g_port) as connection:
#             connection.starttls()
#             connection.login(user=gmail,password=g_password)
#             connection.sendmail(
#                 from_addr=gmail,
#                 to_addrs= birthday_person["email"],
#                 msg= f"Subject:Happy Birthday!\n\n{contents}"
#             )















