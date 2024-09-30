##################### Extra Hard Starting Project ######################
import random
import pandas as pd
import datetime as dt
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

letter_templates_files = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
my_email = "ianleonardmk47@gmail.com"
my_password = "vbwtuxcedgdtfozi"

# reading the csv file
days_data = pd.read_csv("birthdays.csv")

my_dict = days_data.to_dict(orient="records")
list_of_birthdays = []
list_of_names = []
list_of_emails = []
dates = ()

for person in my_dict:
    email = person["email"]
    name = person["name"]
    day = int(person["day"])
    month = int(person["month"])
    dates = (day, month)
    list_of_names.append(name)
    list_of_emails.append(email)
    list_of_birthdays.append(dates)

new_list = [
    {"name": name, "birthday":birthday, "email":email}
    for name, birthday, email in zip(list_of_names, list_of_birthdays, list_of_emails)
]

current_date = dt.date.today()
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

this_day = (current_day, current_month)

for person in new_list:
    if person["birthday"] == this_day:
        with open(file=random.choice(letter_templates_files)) as letter_file:
            letter = letter_file.read()

        modified_letter = letter.replace("[NAME]", person["name"])

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(my_email, my_password)
            server.sendmail(my_email, person["email"], f"Subject:Birthday Wishes \n\n{modified_letter}")

