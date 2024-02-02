import smtplib

# This code fails at the login object!

# create an SMTP object
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS encryption
smtp_obj.starttls()

# login to the email account
smtp_obj.login('jmkimball54@gmail.com', 'password')

# construct the email message
message = "Subject: Email sent by ChatGPT\n\nChatGPT rocks!"

# send the email
smtp_obj.sendmail('jmkimball42@gmail.com', message)

# close the SMTP connection
smtp_obj.quit()