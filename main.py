"""
Python Email
Using SMTP to send an email from Python
멋쟁이 사자처럼 "[심화] 같이 푸는 PYTHON" 강좌 응용.

이메일 제목, 상대방의 이메일, 내용을 input으로 받아서 보내는 프로그램.

Email successfully sent.

# Regular Expression
^로 시작, $로 종료
+는 1회 이상 반복, {2,3}은 2~3회
.은 원래 한 개 문자와 일치, \.은 .자체를 쓰기 위해 사용됨.
"""
import smtplib
from email.message import EmailMessage
import imghdr  # 이미지의 확장자 판단. python 내장
import re  # Regular Expression

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # Gmail port num


def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(msg)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


msg = EmailMessage()
email_subject = input("제목을 입력해주세요. :")
email_to = input("상대방의 이메일을 입력해주세요. :")
email_content = input("내용을 입력해주세요. :")

my_email = "#####EMAIL#####"

# MIME Header의 경우 [] 사용
msg["Subject"] = email_subject
msg["From"] = my_email
msg["To"] = email_to
# email content
msg.set_content(email_content)

with open("test_image.png", "rb") as image:  # rb: read binary
    image_file = image.read()

image_type = imghdr.what('test_image', image_file)
# print(image_type)
msg.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)  # SMTP(server, port)
smtp.login(my_email, "###PASSWORD###")

# Call sendEmail to verify and send an email
sendEmail(email_to)
smtp.quit()
