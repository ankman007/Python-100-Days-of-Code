import smtplib

MY_EMAIL = 'ankitpoudel.seo007@gmail.com'
MY_PASSWORD = 'skkczghdggberkxl'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs='ankeetpoudel2@gmail.com',
        msg='Subject: Second Test Email\n\nThis is awesome.'
    )

# import datetime as dt
# import smtplib
# import random
#
# MY_EMAIL = 'ankitpoudel.seo007@gmail.com'
# MY_PASSWORD = 'skkczghdggberkxl'
#
# if dt.datetime.now().weekday() == 6:
#
#     with open('quotes.txt', 'r') as file:
#         file_contents = file.readlines()
#         quote = random.choice(file_contents)
#
#     with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs='ankeetpoudel2@gmail.com',
#             msg=f'Subject: Upcoming Birthday Email\n\nYour birthday is coming up!! \nHappy birthday!! \nHere is a quote for you: \n{quote}'
#         )

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)








