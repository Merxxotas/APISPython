import json

from jenkinsMain.helpers.name import Name


def generate_name(name):
    name_ids = open("names_ids.txt", "r+")
    str_id = name_ids.readlines()[-1]

    new_name = Name(name, int(str_id))

    name_ids.write(str(new_name.id + 1) + "\n")
    name_ids.close()

    formatted_name = {
        "id": new_name.id,
        "name": new_name.name
    }
    save_data(formatted_name, "names.json")


def save_data(formatted_data: dict, file_name: str):
    json_file = open(file_name, "r")
    data: list = json.load(json_file)
    json_file.close()

    data.append(formatted_data)
    json_string = json.dumps(data)
    json_file = open(file_name, "w")
    json_file.write(json_string)
    json_file.close()


def update_name(id: int, new_name: str):
    json_file = open("names.json", "r")
    data: list = json.load(json_file)
    json_file.close()

    for name in data:
        if name["id"] == id:
            name["name"] = new_name

    json_string = json.dumps(data)
    json_file = open("names.json", "w")
    json_file.write(json_string)
    json_file.close()