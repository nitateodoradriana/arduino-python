import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

SENDGRID_API_KEY = "....."

def trimite_email(data, ora, status):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    from_email = Email("")
    to_email = To("")

    subject = "Notificare: Usa a fost deschisa"
    content = Content("text/plain", f"{status} pe {data} la ora {ora}.")

    mail = Mail(from_email, to_email, subject, content)
    raspuns = sg.client.mail.send.post(request_body=mail.get())

    print(f"Email trimis cu status: {raspuns.status_code}")

