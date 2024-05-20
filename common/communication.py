import csv
import datetime
import json


def parse_communication_protocol(communication_string):
    # Find the start and end positions of the header
    header_start = communication_string.find("--Header:") + len("--Header:")
    header_end = communication_string.find("--EndH")

    # Extract the header and remove leading/trailing whitespaces
    header = communication_string[header_start:header_end].strip()

    # Find the start and end positions of the payload
    payload_start = communication_string.find("--Payload:") + len("--Payload:")
    payload_end = communication_string.find("--EndP", payload_start)

    # Extract the payload and remove leading/trailing whitespaces
    payload = communication_string[payload_start:payload_end].strip()

    # Parse header into an associative array
    header_array = {}
    header_segments = header.split(';')

    payload_array = {}
    payload_segments = payload.split(';')

    return {"Header": header_array, "Payload": payload}


def customHash(text: str):
    hash = 0
    for ch in text:
        hash = (hash * 281 ^ ord(ch) * 997) & 0xFFFFFFFF
    return hash


def find_row(csv_file, search_criteria):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            # Assuming search_criteria is a dictionary with column names as keys
            # and the corresponding values you are searching for
            if all(row[header.index(column)] == str(value) for column, value in search_criteria.items()):
                return row

    return None  # Return None if the row is not found

def find_rows(csv_file, search_criteria = None):
    matching_rows = []

    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            # Assuming search_criteria is a dictionary with column names as keys
            # and the corresponding values you are searching for

            if search_criteria is None: #I just want all tuples
                matching_rows.append(row)
            else:
                if all(row[header.index(column)] == str(value) for column, value in search_criteria.items()):
                    matching_rows.append(row)

    return matching_rows


import csv


def find_rows_v2(csv_file, search_criteria_list=None):
    matching_rows = []

    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            # If no search criteria are provided, return all rows
            if search_criteria_list is None:
                matching_rows.append(row)
            else:
                # Check if the row matches any of the criteria in the list
                row_matches = False
                for search_criteria in search_criteria_list:
                    # Check if all criteria in the dictionary match
                    matches = all(row[header.index(column)] == str(value) for column, value in search_criteria.items())
                    if matches:
                        row_matches = True
                        break
                if row_matches:
                    matching_rows.append(row)

    return matching_rows


def insert_row(csv_file, data_row, custom_id=None):

    if custom_id is not None:
        new_id = custom_id
    else:
        # Determine the last ID in the CSV file and increment it
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            last_row = None
            for row in reader:
                last_row = row
            if last_row is None or is_number(last_row[0]) == False:
                new_id = 1
            else:
                new_id = int(last_row[0]) + 1

    # Insert the new row into the CSV file
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_id] + data_row)

    return new_id


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


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def request_constructor_obj(input_object, header):
    return {
        "header": header,
        "payload": input_object
    }


def request_constructor_str(input_object, header):
    return json.dumps(request_constructor_obj(input_object, header))

def formato_data():
    # Definisci i nomi dei giorni della settimana e dei mesi
    nomi_giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    nomi_mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]

    # Ottieni la data e l'ora attuali
    oggi = datetime.datetime.now()

    # Ottieni il giorno della settimana, il giorno del mese e il mese attuali
    giorno_settimana = nomi_giorni[oggi.weekday()]
    giorno_mese = oggi.day
    mese = nomi_mesi[oggi.month - 1]
    anno = oggi.year

    # Costruisci la stringa con il formato richiesto
    data_formattata = f"{giorno_settimana} {giorno_mese} {mese} {anno}"
    return data_formattata

def get_current_date():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d-%m-%Y")

def filter_dates_after_current(dates):
    current_date = datetime.datetime.now()
    matching_rows = []

    for row in dates:
        row_date = datetime.datetime.strptime(row[1], "%d-%m-%Y %H:%M:%S")
        if row_date > current_date:
            matching_rows.append(row)

    return matching_rows

def loadJSONFromFile(json_file):
    f = open(json_file)
    data = json.load(f)
    f.close()
    return data