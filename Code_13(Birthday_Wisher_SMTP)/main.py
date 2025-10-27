import pandas as pd
import datetime as dt
import os
import random
import smtplib

my_email = "vedsawant07@gmail.com"
my_password = "ubmqdqlttensqtce"

df = pd.read_csv("birthdays.csv")
# converting csv file to dictionary
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for _, data_row in df.iterrows()
}

now = dt.datetime.now()
month = now.month
day = now.day
if (month, day) in birthdays_dict:
    # List all .txt files in the folder
    txt_files = [file for file in os.listdir("letter_templates") if file.endswith(".txt")]
    # Pick a random file
    random_file = random.choice(txt_files)
    # Full path
    random_file_path = os.path.join("letter_templates/", random_file)
    person = birthdays_dict[(month, day)]["name"]
    with open(random_file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", person)
    person_email = birthdays_dict[(month, day)]["email"]
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=person_email,
        msg=f"Subject:Birthday\n\n{content}")
    connection.close()



