import time

from .minutemail import Mail

if __name__ == "__main__":

    mail = Mail()
    print("Email:", mail.get_mail())

    while True:
        if mail.new_message():
            print(mail.fetch_message())

        time.sleep(2)
