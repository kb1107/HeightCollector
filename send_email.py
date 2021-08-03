from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "emailrobot999@gmail.com"
    from_password = "Emailrobot999!"
    to_email = email

    subject = "Height Data"
    message = f"Hey there, your height is <strong>{height} cm</strong>. The average height of all is <strong>{average_height} cm</strong> and that is calculated out of <strong>{count}</strong> people."

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)