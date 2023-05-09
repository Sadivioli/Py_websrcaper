import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from util.util import *

def send_email(to, subject, file_path):

    api_key = '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'

    file_contents = read_file_contents(file_path)

    message = Mail(
        # from_email='your_email@example.com',
        from_email='mmppsender@gmail.com',
        to_emails=to,
        subject=subject,
        html_content=file_contents)
    
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print('Email sent successfully!')
    except Exception as e:
        print('Error sending email:', e)

def send_file_contents_if_long(file_path, to, subject, min_lines):
    # Read the contents of the file
    with open(file_path, 'r') as f:
        contents = f.readlines()
    
    # Check the number of lines
    if len(contents) > min_lines:
        # If the file has more lines than the threshold, send an email
        send_email(to, subject, file_path)
    else:
        print(f"Plik {file_path} nie posiada żadnych nowych informacji.")
