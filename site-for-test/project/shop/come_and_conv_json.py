import json

def come_file():
    """get json file"""
    pass

def open_json():
    """open and read json file"""
    with open("data.txt") as json_file:
        data = json.load(json_file)
        