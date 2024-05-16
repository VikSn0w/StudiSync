import os

from common.communication import find_row, find_rows, insert_row, update_row

ROOT_DIR = os.path.abspath(os.curdir)

DB = {
    "RICHIESTE_DATE_ESAMI": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiesteDateEsami.csv'),
    "RICHIESTE_PRENOTAZIONI_ESAMI": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiestePrenotazioneEsami.csv'),
    "CORSI": os.path.join(ROOT_DIR, 'db', 'esami', 'corsi.csv'),
    "APPELLI": os.path.join(ROOT_DIR, 'db', 'esami', 'appelli.csv'),
    "LAUREA": os.path.join(ROOT_DIR, 'db', 'esami', 'laurea.csv'),
    "SEGRETERIA": os.path.join(ROOT_DIR, 'db', 'users', 'office.csv'),
    "STUDENTI": os.path.join(ROOT_DIR, 'db', 'users', 'students.csv')
}

def default_case():
    return "Method not implemented"

def GetStudente(payload):
    result_row = find_row(DB["STUDENTI"], {"Matricola": payload["Matricola"]})
    if result_row:
        return {"result":result_row}
    else:
        return {"result":"false"}

def GetAppello(payload):
    result_row = find_row(DB["APPELLI"], {"ID": payload["ID"]})
    if result_row:
        return {"result":result_row}
    else:
        return {"result":"false"}


def StudentsLogin(payload):
    result_row = find_row(DB["STUDENTI"], {"Matricola": payload["Matricola"]})
    if result_row:
        if "Password" in payload:
            if str(result_row[4]) == str(payload["Password"]):
                result_row.append(find_row("db/esami/laurea.csv", search_criteria={"ID": result_row[5]}))
                print(result_row)
                result_row.append(find_rows("db/esami/corsi.csv", search_criteria={"Laurea": result_row[5]}))
                return result_row
            else:
                return False
        else:
            return False
    else:
        return False

def OfficeLogin(payload):
    result_row = find_row(DB["SEGRETERIA"], {"Email": payload["Email"]})
    if result_row:
        if "Password" in payload:
            if str(result_row[4]) == str(payload["Password"]):
                return result_row
            else:
                return False
        else:
            return False
    else:
        return False

def InsertLaurea(payload):

    result_row = find_row(DB["LAUREA"], {"ID": payload["MtrLaurea"]})
    if result_row:
       return {"result": result_row}
    else:
        insert_row(DB["LAUREA"], [str(payload["NomeLaurea"])], custom_id=payload["MtrLaurea"])
        return {"result": "True"}

def GetLauree():
    result_row = find_rows(DB["LAUREA"], None)
    if result_row:
        return {"result": result_row}
    else:
        return False

def InsertCorso(payload):
    result_row = find_row(DB["CORSI"], {"ID": payload["IdCorso"]})
    if result_row:
        return {"result": result_row}
    else:
        insert_row(DB["CORSI"],
                   [payload["CFU"], payload["NomeCorso"], payload["NomeProfessore"], payload["Laurea"]],
                   custom_id=payload["IdCorso"])
        return {"result": "True"}

def GetRichiesteDateEsamiNonEvase():
    result_row = find_rows(DB["RICHIESTE_DATE_ESAMI"], {"isAccettata": "?"})
    if result_row:
        final_row = []
        for row in result_row:
            tmp = []
            tmp.append(row[0])
            tmp.append(row[1])
            tmp.append(row[2])
            tmp.append(row[3])
            studente = GetStudente({"Matricola":row[1]})
            if studente["result"] != "false":
                tmp.append(studente["result"][1])
                tmp.append(studente["result"][2])
            else:
                tmp.append("ERRORE")
                tmp.append("ERRORE")
            final_row.append(tmp)
        return {"result": final_row}
    else:
        return {"result": "false"}

def GetRichiestePrenotazioniAppelliNonEvase():
    result_row = find_rows(DB["RICHIESTE_PRENOTAZIONI_ESAMI"], {"isAccettata": "?"})
    if result_row:
        final_row = []
        for row in result_row:
            tmp = []
            tmp.append(row[0])
            tmp.append(row[1])
            tmp.append(row[3])
            studente = GetStudente({"Matricola":row[1]})
            if studente["result"] != "false":
                tmp.append(studente["result"][1])
                tmp.append(studente["result"][2])
            else:
                tmp.append("ERRORE")
                tmp.append("ERRORE")
            appello = GetAppello({"ID": row[2]})
            if appello["result"] != "false":
                tmp.append(appello["result"][1])
                tmp.append(appello["result"][2])
            else:
                tmp.append("ERRORE")
                tmp.append("ERRORE")
            final_row.append(tmp)
        return {"result": final_row}
    else:
        return {"result": "false"}

def AggiornaRichiestaData(payload):
    update_row(csv_file=DB["RICHIESTE_DATE_ESAMI"], row_id=payload["ID"], column_name="isAccettata", new_value=payload["isAccettata"])
    return {"result": "OK"}

def AggiornaRichiesteAppelli(payload):
    update_row(csv_file=DB["RICHIESTE_PRENOTAZIONI_ESAMI"], row_id=payload["ID"], column_name="isAccettata", new_value=payload["isAccettata"])
    return {"result": "OK"}

def method_switch(method, payload):
    match method:

        case "StudentsLogin":
            return StudentsLogin(payload)
        case "OfficeLogin":
            return OfficeLogin(payload)

        case "InsertLaurea":
            return InsertLaurea(payload)
        case "GetLauree":
            return GetLauree()

        case "InsertCorso":
            return InsertCorso(payload)

        case "GetRichiesteDateEsamiNonEvase":
            return GetRichiesteDateEsamiNonEvase()

        case "GetRichiestePrenotazioniAppelliNonEvase":
            return GetRichiestePrenotazioniAppelliNonEvase()

        case "AggiornaRichiestaData":
            return AggiornaRichiestaData(payload)

        case "AggiornaRichiesteAppelli":
            return AggiornaRichiesteAppelli(payload)

        case _:
            return default_case()

