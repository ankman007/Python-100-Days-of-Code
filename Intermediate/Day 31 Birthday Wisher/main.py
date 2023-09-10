import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = 'ankitpoudel.seo007@gmail.com'
MY_PASSWORD = 'skkczghdggberkxl'

birthdays_info = pd.read_csv('birthdays.csv').to_dict(orient='records')
birthdays_list = {}

for i in birthdays_info:
    key = (i['month'], i['day'])
    value = (i['email'], i['name'])
    birthdays_list[key] = value


current_month = dt.datetime.now().month
current_day = dt.datetime.now().day
random_num = random.randrange(1, 4)

if (current_month, current_day) in birthdays_list:
    recipient_name = birthdays_list[(current_month, current_day)][1]
    recipient_email = birthdays_list[(current_month, current_day)][0]

    with open(file=f'letter_templates/letter_{random_num}.txt', mode='r') as file:
        template = file.read()

    edited_template = template.replace('[NAME]', recipient_name)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient_email,
            msg=f'Subject: Happy Birthday!!!\n\n{edited_template}'
        )





