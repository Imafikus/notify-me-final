import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

def send_mail(body, target_mail, target_subject):
    """
    Send body to the target_mail
    """
    print("Send mail...")

    fromaddr = "MAIL"
    toaddr = target_mail
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Site changed - " + target_subject; 
    
    msg.attach(MIMEText(body, 'html'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "PASS")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()