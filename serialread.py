# UTILIZZO:
# 1. Modificare le variabili "port" e "baud" in base alla vostra macchina e Arduino
# 2. Lanciare il programma da terminale con "python serialread.py"
# 3. Seguire le indicazioni
#
# Il nome del file di salvataggio va scritto SENZA estensione (viene salvato in .csv)

import serial, csv, time

port = '/dev/ttyACM0'
baud = 115200

def delay(tempo):
    t0 = time.time()
    while (time.time() - t0) < tempo:
        x = 0 # modo brutto per far passare il tempo


tempo = input('Inserisci intervallo di tempo (secondi): ')

registro = [] # matrice per salvare i dati

## Inizializzazione porta seriale
ser = serial.Serial(port, baudrate=baud)
delay(1) # serve per far resettare bene il buffer
ser.reset_input_buffer()
y = ser.readline() # scarta il primo valore dal buffer

print 'Sto ricevendo i dati..'
t0 = time.time()
i = 1
while (time.time() - t0) < tempo:
    x = ser.readline()
    registro.append([i, x[:-2]]) # x[:-2] pulisce i caratteri di newline
    i += 1

print "Fatto!"

filename = raw_input('Inserisci nome del file di salvataggio: ') + ".csv"
writer = csv.writer(open(filename, 'w'))
writer.writerows(registro)
