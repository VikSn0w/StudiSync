from common.communication import find_row, find_rows


def default_case():
    return "Method not implemented"

def StudentsLogin(payload):
    result_row = find_row("db/users/students.csv", {"Matricola": payload["Matricola"]})
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
    result_row = find_row("db/users/office.csv", {"Email": payload["Email"]})
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


def method_switch(method, payload):
    match method:
        case "StudentsLogin":
            return StudentsLogin(payload)
        case "OfficeLogin":
            return OfficeLogin(payload)
        case _:
            return default_case()

