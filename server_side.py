import common.communication
from common.communication import find_row
from common.communication import customHash


def default_case():
    return "Method not implemented"

def StudentsLogin(payload):
    result_row = find_row("db/users/students.csv", {"Matricola": payload["Matricola"]})
    if "Password" in payload:
        print(payload["Password"], result_row[4])
        if str(result_row[4]) == str(payload["Password"]):
            return result_row if result_row else False
        else:
            return False
    else:
        return False

def OfficeLogin(payload):
    result_row = find_row("db/users/office.csv", {"Email": payload["Email"]})
    if "Password" in payload:
        print(payload["Password"],result_row[4])
        if str(result_row[4]) == str(payload["Password"]):
            return result_row if result_row else False
        else:
            return False
    else:
        return False


def method_switch(method, payload):
    switch_dict = {
        "StudentsLogin": StudentsLogin(payload),
        "OfficeLogin": OfficeLogin(payload),
    }

    # Use get() to handle default case
    selected_case = switch_dict.get(method,default_case)

    # Call the selected case function
    return selected_case