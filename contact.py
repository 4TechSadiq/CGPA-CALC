import smtplib

USER = ""
PASSWORD = ""

def send_mail(name:str, mail:str, msg: str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs="", msg=f"Subject:Contact CGPA!!\n\n Name:{name}\n Mail:{mail} \n Message:{msg}")
        
        return True
