import serial
from goosh import trimite_in_sheet
from send_grid_emails import trimite_email

arduino = serial.Serial('COM11', 9600)

def comanda_trm(comanda):
    arduino.write(comanda.encode() + b'\n')
    print(f"Comandă trimisă: {comanda}")

    if comanda == "deschide":
        trimite_in_sheet("Usa deschisa")
