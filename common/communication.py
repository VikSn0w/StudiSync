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