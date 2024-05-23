import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def SendEmailWithAttachment(FileToSend, MessageSubject, debug=False, UserList="Nulled"):
    if debug is True and "Nulled" in UserList:
        recipients = 'useremail@mailserver.com'
    elif debug is True and "Nulled" not in UserList:
        recipients = UserList
    else:
        recipients = ['user@useremail.com','user2@useremail.com']
    fileToSend = str(FileToSend)
    msg = MIMEMultipart()
    msg["From"] = "outsideuser@mailserver.com"
    msg['To'] = ", ".join(recipients)
    msg["Subject"] = str(MessageSubject)
    msg.preamble = "Very Important, Do not ignore."
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)

    server = smtplib.SMTP("mailrelay.mailserver.net:25")
    server.starttls()
    server.sendmail(msg["From"], recipients, msg.as_string())
    server.quit()


def SendEmailWithoutAttachmentGeneric(MessageSubject, EmailBodyText, Receivers="None"):
    EventsToSend = str(EmailBodyText)
    if Receivers == "None":
        recipients = ['user@useremail.com','user2@useremail.com']
    else:
        recipients = Receivers
    msg = MIMEMultipart()
    msg["From"] = "user@mailserver.com"
    msg['To'] = ", ".join(recipients)
    msg["Subject"] = str(MessageSubject)
    part1 = MIMEText(EventsToSend, 'plain')
    msg.attach(part1)
    msg.preamble = "Very Important, Do not ignore."

    server = smtplib.SMTP("mailrelay.mailserver.net:25")
    server.starttls()
    server.sendmail(msg["From"], recipients, msg.as_string())
    server.quit()


def SendEmailForVMInventory(FileToSend, MessageSubject, ListUsers="none"):
    fileToSend = str(FileToSend)
    if "none" in ListUsers:
        recipients = ['user@useremail.com','user2@useremail.com']
    else:
        recipients = ListUsers
    msg = MIMEMultipart()
    msg["From"] = "user@mailserver.com"
    msg['To'] = ', '.join(recipients)
    msg["Subject"] = str(MessageSubject)
    msg.preamble = "Very Important, Do not ignore."

    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)

    server = smtplib.SMTP("mailrelay.mailserver.net:25")
    server.starttls()
    server.sendmail(msg["From"], recipients, msg.as_string())
    server.quit()
