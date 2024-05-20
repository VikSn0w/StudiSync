import csv
import json
import os

from common.communication import find_rows_v2

ROOT_DIR = os.path.abspath(os.curdir)

DB = {
    "PRENOTAZIONI_ESAMI": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'prenotazioniEsame.csv'),
    "RICHIESTE_DATE_ESAMI": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiesteDateEsami.csv'),
    "RICHIESTE_PRENOTAZIONI_ESAMI": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiestePrenotazioniEsami.csv'),
    "CORSI": os.path.join(ROOT_DIR, 'db', 'esami', 'corsi.csv'),
    "APPELLI": os.path.join(ROOT_DIR, 'db', 'esami', 'appelli.csv'),
    "LAUREA": os.path.join(ROOT_DIR, 'db', 'esami', 'laurea.csv'),
    "SEGRETERIA": os.path.join(ROOT_DIR, 'db', 'users', 'office.csv'),
    "STUDENTI": os.path.join(ROOT_DIR, 'db', 'users', 'students.csv')
}

if __name__ == '__main__':
    result_row = find_rows_v2(DB["RICHIESTE_DATE_ESAMI"],[{"matricolaRichiedente": "0124002584"}, {"isAccettata": "?"}])
    print(result_row)