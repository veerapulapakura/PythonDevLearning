# Email sending

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Veera Pulapakura'
email['to'] = 'veera.ratna@gmail.com'
email['subject'] = ' You won 1000 rupees'
email.set_content('this is the basic email text')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('veera.ratna@gmail.com', 'Raju1236!')
    smtp.send_message(email)
    print('All is good but chnaged now')