import json


def display_json():
    with open('monster.json', 'r') as f:
        json_content = json.load(f)
        print(json_content)


def display_name_from_json():
    with open('monster.json', 'r') as f:
        json_content = json.load(f)
        # Calling specific .json key
        print("Welcome", json_content['monsterName'])


if __name__ == "__main__":
    # display_json()
    display_name_from_json()
