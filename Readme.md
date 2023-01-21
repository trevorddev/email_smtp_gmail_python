### Installation

```shell
pip install -r requirements.txt
```

### Usage

```shell
python email_sender.py --help

Usage: email_sender.py [OPTIONS] SENDER PASSWORD DISPLAY_NAME REPLY_TO TO
                       SUBJECT BODY

Options:
  --cc TEXT
  --bcc TEXT
  -a, --attachment FILENAME
  --help                     Show this message and exit.
```

Note: 

- sender was an email that used for SMTP authentication
- see this link for password https://support.google.com/mail/answer/7126229?visit_id=638095331531397460-2850466871&p=BadCredentials&rd=2#cantsignin&zippy=%2Ci-cant-sign-in-to-my-email-client
- all arguments are strings.
- the script will print:
  - 0,  => if no error occurred
  - 1, A message => if an error occurred
- options cc, bcc, attachment can be used multiple times. That means, you can have multiple cc, bcc and also the attachment.
- make sure to add a full path into attachment.

Here is the example how to invoke the script

```shell
 python email_sender.py sender@gmail.com "your password" "Your display" reply_to@gmail.com to@email.com "my subject" "this is a hello world string, hello hello hello. hello" -a "/home/home/g1051.png" -a "/home/homefolder/notify-con.png" --attachment "/home/homefolder/2023-01-01_13-38-13.mp4" --cc cc1@gmail.com --cc cc2@gmail.com
```

