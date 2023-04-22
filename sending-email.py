import smtplib

# Set up the SMTP server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
from_email = input('Enter your email: ')
from_password = input('Enter your password: ') # get from https://myaccount.google.com/apppasswords
to_email = input('Enter the recipient\'s email: ')
smtp_server.login(from_email, from_password)

# Compose the email message
from_address = from_email
to_address = to_email
subject = 'Test email'
body = 'This is a test email sent from Python.'
message = f'Subject: {subject}\n\n{body}'

# Send the email
smtp_server.sendmail(from_address, to_address, message)

# Close the SMTP server
smtp_server.quit()