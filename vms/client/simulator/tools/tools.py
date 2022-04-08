import json

def config_load(filename:str) -> dict:
    config_data = {}
    print(filename)
    with open(filename) as config_file:
        config_data = json.load(config_file)

    return config_data

