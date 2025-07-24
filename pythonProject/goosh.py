import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from send_grid_emails import trimite_email

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Autentificare cu cheia de serviciu folosind datele JSON
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_dict({

}, SCOPE)

client = gspread.authorize(CREDENTIALS)
sheet = client.open_by_key("").sheet1


def trimite_in_sheet(status):
    now = datetime.datetime.now()
    data = now.strftime("%Y-%m-%d")
    ora = now.strftime("%H:%M:%S")
    sheet.append_row([data, ora, status])

    trimite_email(data, ora, status)


