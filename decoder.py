import sys
import os
import json
import win32com.client

# set config file
config_file = "./config.json"
config_data = {}
# create speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")

if (os.path.isfile(config_file)):
    # load config
    with open(config_file) as json_data:
        config_data = json.load(json_data)
else:
    print("Something is wrong.")
    sys.exit(0)

def decode(speech):

    if (speech == "stop listening"):
        speaker.Speak("Goodbye")
        sys.exit(0)
    else:
        if "call me" in speech:
            name = speech.split(" me ")[1]
            response = "Okay {}".format(name)
            speaker.Speak(response)
            # build the data
            config_data["name"] = name

            # write name to config file
            with open(config_file, 'w') as outfile:
                json.dump(config_data, outfile)
        elif "what's my name" in speech:
            name = config_data["name"]
            response = "Your name is {}".format(name)
            speaker.Speak(response)
    return