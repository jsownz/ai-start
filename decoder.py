import sys
import os
import json
import config
import speaker

def learn_name(name):
    # build a response
    response = "Okay {}".format(name)
    # say it
    speaker.speak(response)
    # save the data
    config.save_config("name",name)

def decode(speech):
    # set config data
    config_data = config.get_config()

    if (speech == "stop listening"):
        speaker.speak("Goodbye")
        sys.exit(0)
    else:
        if "call me" in speech:
            # get name from text
            name = speech.split("all me ")[1]
            learn_name(name)
        if "my name is" in speech:
            # get name from text
            name = speech.split("name is ")[1]
            learn_name(name)
        elif "what's my name" in speech:
            try:
                # using a try/catch here to see if the data exists in the config
                name = config_data["name"]
                response = "Your name is {}".format(name)
                speaker.speak(response)
            except KeyError:
                speaker.speak("I don't know what to call you yet.")
    return