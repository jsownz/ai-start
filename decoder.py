import sys
import os
import json
import win32com.client
import config

# create speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def decode(speech):
    # set config data
    config_data = config.get_config()

    if (speech == "stop listening"):
        speaker.Speak("Goodbye")
        sys.exit(0)
    else:
        if "call me" in speech:
            name = speech.split(" me ")[1]
            response = "Okay {}".format(name)
            speaker.Speak(response)
            # save the data
            config.save_config("name",name)
        elif "what's my name" in speech:
            try:
                name = config_data["name"]
                response = "Your name is {}".format(name)
                speaker.Speak(response)
            except KeyError:
                speaker.Speak("I don't know what to call you yet.")
    return