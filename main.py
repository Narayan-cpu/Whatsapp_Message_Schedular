from twilio.rest import Client
from datetime import datetime,timedelta
import time
import os

Account_Sid = os.getenv("Account_sid")
Account_tok = os.getenv("Account_tok")

client = Client(Account_Sid, Account_tok)

def send_Whatsapp_message(recepent_number,message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recepent_number}'
        )
        print(f"Message sent Successfully ! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")
    
name=input("Enter your name of recepent: ")
recepent_number=input("Enter the recepent Whatsappnumber (Eg: +91XXXXXXXXXX): ")
message_body=input("Enter the message body: ")

date_str=input("Enter the date in YYYY-MM-DD format: ")
time_str=input("Enter the time in HH:MM format: ")
schedule_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
curr_date_time = datetime.now()

time_diff = schedule_time - curr_date_time
delayseconds = time_diff.total_seconds()
if time_diff.total_seconds() < 0:
    print("The scheduled time is in the past. Please enter a future date and time.")
else:
    print(f"Message Schedule to be sent to {name} on {schedule_time}")

    time.sleep(delayseconds)

    send_Whatsapp_message(recepent_number,message_body)

