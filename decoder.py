import sys
import os
import json
import config
import speaker

def decode(speech):
    # set config data
    config_data = config.get_config()

    if (speech == "stop listening"):
        speaker.speak("Goodbye")
        sys.exit(0)
    else:
        if "call me" in speech:
            name = speech.split(" me ")[1]
            response = "Okay {}".format(name)
            speaker.speak(response)
            # save the data
            config.save_config("name",name)
        elif "what's my name" in speech:
            try:
                name = config_data["name"]
                response = "Your name is {}".format(name)
                speaker.speak(response)
            except KeyError:
                speaker.speak("I don't know what to call you yet.")
    return