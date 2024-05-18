import csv
import json
import os

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


def update_row(csv_file:str, row_id:str, column_name:str, new_value:str):
    # Read the CSV file and store its contents in a list of dictionaries
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)

    # Find the row with the given ID
    for row in rows:
        if row['ID'] == row_id:
            # Update the value in the specified column
            row[column_name] = new_value
            break
    else:
        print(f"Row with ID {row_id} not found.")
        return

    # Write the updated contents back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        fieldnames = csv_reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Value in row {row_id}, column {column_name} updated to {new_value}.")

if __name__ == '__main__':
    ciao = json.loads('{"dates": [["2", "11-06-2024 09:00:00", "MAT1"], ["3", "10-06-2024 09:00:00", "MAT1"], ["4", "12-06-2024 09:00:00", "MAT1"]]}')
    print(ciao)