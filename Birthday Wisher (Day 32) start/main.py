# import smtplib
# my_email = "ianleonardmk47@gmail.com"
# password = "vbwtuxcedgdtfozi"
#
#
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="mandegemasebu@yahoo.com", msg="Subject:Greetings \n"
#                                                                                 "\nHello")
## connection.close()
#
# import datetime as dt
#
# from dateutil.rrule import weekday
#
# now = dt.datetime.now()
# year = now.year
# week_day = now.weekday()
# print(week_day)
#
# # date_of_birth = dt.date(year = 2002, month=2, day=5)
# # print(date_of_birth)

import smtplib
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()

email = 'ianleonardmk47@gmail.com'
password = 'vbwtuxcedgdtfozi'

if day_of_week == 6:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.starttls()
        connection.login(email, password )
        connection.sendmail(from_addr=email, to_addrs="mandegemasebu@yahoo.com", msg="Subject: Morning Alarm!\n\nHey, Wake up!")
        connection.close()