import smtplib
my_email = "appbreweryinfo@gmail.com"
password = "ildqyaojtomcgauu"


connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com", msg="Hello")
connection.close()