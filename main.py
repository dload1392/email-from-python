"""
Python Email
Using SMTP to send emails from Python
멋쟁이 사자처럼 "[심화] 같이 푸는 PYTHON" 강의 참조.
"""
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465     # Gmail port num

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)      # SMTP(server, port)
smtp.login("id", "pw")
smtp.send_message()
smtp.quit()

