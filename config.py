import sys
import os
import json

config_file = "./config.json"
config_data = {}

def get_config():
    global config_data
    if (os.path.isfile(config_file)):
        # load config
        with open(config_file) as json_data:
            config_data = json.load(json_data)
    else:
        with open(config_file, 'w') as outfile:
            json.dump(config_data, outfile)

    return config_data

def save_config(field,value):
    global config_data
    config_data[field] = value
    with open(config_file, 'w') as outfile:
            json.dump(config_data, outfile)
