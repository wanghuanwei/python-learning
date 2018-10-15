import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header

def sendmail(from_account, to_account, from_pass,subject,content):
    logging.info('start to sendmail,from %s, to %s ,title %s' %(from_account,to_account,subject))
    mail_client=smtplib.SMTP_SSL('smtp.qq.com', 465)
    mail_client.login(from_account,from_pass)

    mail_msg = MIMEText(content, 'plain', 'utf-8')
    mail_msg['From']=Header(from_account, 'utf-8')
    # mail_msg['To']=Header(to_account, 'utf-8')
    mail_msg['Subject']=Header(subject, 'utf-8')

    mail_client.sendmail(from_account,to_account,mail_msg.as_string())
    logging.info('sendmail success')
    mail_client.quit()

logging.basicConfig(level= logging.INFO)
if __name__ == '__main__':
    pass
