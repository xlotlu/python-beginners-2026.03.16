"""
exemplu de automatizare de trimitere de mail-uri cu smtp,
creare de mesaj dintr-un template html
și încărcarea variabilelor din csv.
"""

# pentru a trimite un e-mail este nevoie de două module / clase:

import smtplib # pentru interacțiune cu serverul (dacă folosește smtp)
from email.message import EmailMessage # pentru a crea e-mailul propriu-zis

# importăm și csv pentru a stoca sursa de date pe baza căreia automatizăm
import csv

# importăm variabilele de configurație 
from config import *


class Eh:
    def __init__(self, host, port):
        pass
    def login(self, username, pswd):
        pass
    def __enter__(self, *args, **kwargs):
        return self
    def __exit__(self, *args, **kwargs):
        pass
    def send_message(self, msg):
        print(msg)
smtplib.SMTP_SSL = Eh

def send_emails(conn, template, subject, dataset):
    """
    given the SMTP connection `conn` and the str `template`,
    apply `.format()` on it with the rows from the given `dataset`,
    and send the resulting e-mail messages. 
    """
    pass

    # we construct a message for each row in the dataset
    for row in dataset:
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = row['email']
        msg["Subject"] = subject

        # plain-text fallback, should be included
        msg.set_content(
            "This is an HTML message. Please enable HTML in your e-mail client."
        )

        # notă: ** despachetează un dicționar drept keyword-arguments
        html_content = template.format(**row)

        msg.add_alternative(html_content, subtype="html")

        # and finally send the message
        smtp.send_message(msg)

# exemplu de template html:
template = """
<!DOCTYPE html>
<html>
    <body style="font-family: Arial, sans-serif;">
        <h2 style="color: #4CAF50;">Salutare {name}</h2>
        <p>Acesta este un mesaj automatizat.</p>
    </body>
</html>
"""

## alternativ, acesta poate fi citit dintr-un fișier
## salvat spre exemplu din word. (poate necesita clean-up manual.)
# with open("/tmp/template.html") as f:
#    template = f.read()

subject = "Salutare, acesta este subiectul e-mailului"
data = [
    {"email": "addr1@example.com", "name": "Domnul Exemplu"},
    {"email": "addr2@example.com", "name": "Doamna Exemplu"},
]

## alternativ, citește dataset-ul dintr-un csv.
## este important ca numele coloanelor să se potrivească cu cele folosite
## în template.
with open("dataset.csv") as f:
    data = csv.DictReader(f)

    # (în cazul în care dataset-ul este imens, pentru eficiență,
    # am pune acest `with` în jurul chemării funcției `send_emails`)

    # aceste variabile sunt importate din config
    with smtplib.SMTP_SSL(HOST, PORT) as smtp:
        #smtp.starttls() # posibil necesar
        smtp.login(EMAIL, PASSWORD)

        send_emails(smtp, template, subject, data)
