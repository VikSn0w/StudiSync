import csv


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

def object_to_json_string(obj):
    # Check if the object is a dictionary
    if isinstance(obj, dict):
        items = []
        for key, value in obj.items():
            items.append(f'"{key}": "{value}"')
        return "{" + ", ".join(items) + "}"

    # Handle other types as needed (this is a basic example)
    # You may need to add more logic for other data types
    elif isinstance(obj, (str, int, float, bool, list)):
        return str(obj)

    # Raise an exception for unsupported types
    else:
        raise TypeError(f"Unsupported type: {type(obj)}")

def json_string_to_object(json_string):
    # Ensure the input is a string
    if not isinstance(json_string, str):
        raise TypeError("Input must be a string")

    # Remove leading and trailing whitespaces
    json_string = json_string.strip()

    # Check if the JSON string starts and ends with curly braces
    if json_string[0] == "{" and json_string[-1] == "}":
        # Split the string into key-value pairs
        key_value_pairs = json_string[1:-1].split(",")

        # Create a dictionary from key-value pairs
        result_dict = {}
        for pair in key_value_pairs:
            key, value = pair.split(":", 1)
            result_dict[key.strip(' "')] = value.strip(' "')

        return result_dict
    else:
        raise ValueError("Invalid JSON string")

def customHash(text:str):
  hash=0
  for ch in text:
    hash = ( hash*281  ^ ord(ch)*997) & 0xFFFFFFFF
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