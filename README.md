# WhatsApp Message Scheduler 📅💬

Ever wanted to send your future self (or a forgetful friend) a WhatsApp message at the perfect time? Well, you're in luck! This **WhatsApp Message Scheduler** lets you automate sending messages using Python and Twilio. Forget setting alarms to remind yourself to send "Happy Birthday!" at midnight—let this script do the heavy lifting for you. 🎉

---

## Features 🚀

- 📅 Schedule WhatsApp messages to send at a specific time.
- 🛠 Built with Python (because who doesn't love Python?).
- 🤖 Powered by Twilio API for seamless WhatsApp message delivery.
- 💬 Send reminders, jokes, or even passive-aggressive "Did you finish that task yet?" messages. 

---

## Prerequisites 🧐

Before we dive into scheduling your messages, you'll need a few things:

1. **Python** installed on your machine. (No Python? No party. 🐍)
2. A **Twilio account** (because Twilio is the messaging magician here 🎩✨).
3. Credentials for Twilio, which include:
   - **Account SID**
   - **Auth Token**
   - **Twilio Sandbox phone number** (It’s like a VIP pass for WhatsApp messaging 🛂).

---

## Setting Up Twilio 🕵️‍♀️

If you don’t have a Twilio account yet, here’s how to get started:

1. Head over to [Twilio's website](https://www.twilio.com/) and sign up. It's free to start!
2. Once logged in, grab your **Account SID** and **Auth Token** from the Twilio Console.
3. Activate the **Twilio Sandbox for WhatsApp** by following [this guide](https://www.twilio.com/docs/whatsapp/sandbox). You’ll need to join the sandbox by sending a message to Twilio’s number—don’t worry, they’re friendly. 🤝

---

## Installation 🛠

1. Clone this repository to your machine:

   ```bash
   git clone https://github.com/Narayan-cpu/Whatsapp_Message_Schedular.git
   cd Whatsapp_Message_Schedular
   ```

2. Install the required Python dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Open the script file and enter your Twilio credentials (Account SID, Auth Token, and Twilio Sandbox phone number). Don’t worry, your secrets are safe... as long as you don’t share them in public! 🙈

---

## Usage 🎯

1. Run the script:

   ```bash
   python scheduler.py
   ```

2. Follow the prompts to:
   - Enter the recipient's WhatsApp number (don’t forget the country code!).
   - Type your message (keep it classy, folks).
   - Schedule the time to send your message. (Time travel not included. ⏳)

3. Sit back, relax, and let the script do its thing. Your message will be sent right on schedule. 🎉

---

## Example 🤓

Here’s what using the script might look like:

```plaintext
Enter the recipient's WhatsApp number (with country code): +1234567890
Enter your message: Don't forget to bring snacks for the meeting!
Enter the scheduled time (YYYY-MM-DD HH:MM:SS): 2025-04-12 14:00:00
Your message is scheduled! 🎉
```

---

## Why Use This? 🤔

- Because you're tired of forgetting birthdays. 🎂
- Because you want to be the friend who always sends that perfectly-timed meme. 🐸
- Or simply because you can. 💪

---

## Contributing 🤝

Got a great idea to make this even better? Fork the repo, make your changes, and send a pull request. Together, we can make the world a more punctual place. 🌍

---

## Disclaimer ⚠️

This script uses Twilio's sandbox, so it’s limited to pre-approved numbers and non-commercial use. If you want to use it for production purposes, you'll need to upgrade your Twilio account (and maybe send them a thank-you card 📬).


---

Enjoy scheduling messages responsibly! And remember: with great power comes great responsibility (to not spam people at 3 a.m.). 🌟

---

Let me know if you'd like to add or tweak anything!
