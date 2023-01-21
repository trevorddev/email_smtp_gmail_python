from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import click
import smtplib


@click.command()
@click.argument("sender")
@click.argument("password")
@click.argument("display_name")
@click.argument("reply_to")
@click.argument("to")
@click.option("--cc", multiple=True, required=False)
@click.option("--bcc", multiple=True, required=False)
@click.argument("subject")
@click.argument("body")
@click.option("-a", "--attachment", required=False, type=click.File("rb"), multiple=True)
def send_mail(
        sender,
        password,
        display_name,
        reply_to,
        to,
        cc,
        bcc,
        subject,
        body,
        attachment
):
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()
        session.login(sender, password)

        message = MIMEMultipart()
        message["FROM"] = f"{display_name} <{sender}>"
        message["TO"] = to
        message["CC"] = ", ".join([item for item in cc])
        message.add_header("reply-to", reply_to)
        message["SUBJECT"] = subject
        message.attach(MIMEText(body, "plain"))

        to_address = [to] + list(bcc)

        if attachment:
            for att in attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(att.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment;filename={Path(att.name).name}")
                message.attach(part)

        session.sendmail(sender, to_address, message.as_string())
        session.quit()
        print("0, ")
        return 0, ""
    except smtplib.SMTPAuthenticationError:
        print("1, Authentication error")
        return 1, "Authentication error"
    except Exception as e:
        print(f"1, Unknown error: {str(e)}")
        return 1, f"Unknown error: {str(e)}"


if __name__ == '__main__':
    send_mail()
