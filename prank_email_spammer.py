import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from platform import python_version


server = "smtp.mail.ru"
user = ""
password = ""

wish_subject = ""
wish_text = ""
recipients = []

try:
    def choose_platform():
        while True:
            global server
            print("Выберете платформу своего почтового ящика с которого будут отсылаться письма")
            print("Яндекс - 1, Mail - 2, Gmail - 3, Rambler - 4")
            print("Введите цифру")
            platform = int(input())
            if platform == 1:
                server = "smtp.yandex.ru"
                break
            elif platform == 2:
                server = "smtp.mail.ru"
                break
            elif platform == 3:
                server = "smtp.gmail.com"
                break
            elif platform == 4:
                server = "smtp.rambler.ru"
                break
            else:
                print("Такого почтового ящика ненайдено")
                print()

                
    def input_info():
        print()
        global user
        global password
        global recipients
        global wish_subject
        global wish_text
        global email_count
        user = input("Введите свою почту (обязательно почта Mail) с которой будут осылаться письма: ")
        password = input("Введите пароль от почты: ")
        recipient = input("Введите почтовый ящик жертвы: ")
        recipients.append(recipient)
        print()
        wish_subject = input("Введите тему письма: ")
        wish_text = input("Введите текст письма: ")
        email_count = int(input("Введите количество писем, которые будут отправлены жертве: "))
        

    #choose_platform()
    input_info()


    sender = user
    subject = wish_subject
    text = wish_text + " <br> <br> <i>Это письмо отправлено с помощью <b>prank email spammer</b></i>"
    html = '<html><head></head><body><p>' + text + '</p></body></html>'


    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = "Prank email spammer <" + sender + ">"
    msg["To"] = ", ".join(recipients)
    msg["Reply-To"] = sender
    msg["Return-Path"] = sender
    msg["X-Mailer"] = "Prank email spammer"

    part_text = MIMEText(text, "plain")
    part_html = MIMEText(html, "html")


    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    #print("Инфа - ", user, "_", password, "_", server)
    mail.login(user, password)

    for i in range(email_count):
        mail.sendmail(sender, recipients, msg.as_string())
        print("Письмо №", (i + 1), " отправлено!")

    print("Все письма успешно отправлены!")
    
    mail.quit()


except:
    print("Что-то пошло не так!")

#print()
#input("Нажмите Enter, чтобы выйти")
