import speech_recognition as sr
import json
import os
import sys
import win32com.client

# set config file
config_file = "./config.json"
config_data = {}
# declare recognizer
r = sr.Recognizer()
# create speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")

if (os.path.isfile(config_file)):
    # load config
    with open(config_file) as json_data:
        config_data = json.load(json_data)
else:
    # didnt find a config file, get mic selection
    print("No config file found. Please select a microphone to use")
    print("-------------------------------------------------------")
    # loop over mic options and print them out nicely
    for index,choice in enumerate(sr.Microphone.list_microphone_names()):
        print("%s - %s" % (index,choice))
    
    # get user mic choice
    mic_choice = int(input("Select the index of the mic: "))

    # build the data
    config_data['microphone_index'] = mic_choice

    # the create config file
    # and write mic choice to it
    with open(config_file, 'w') as outfile:
        json.dump(config_data, outfile)

# declare mic to use
mic = sr.Microphone(device_index=int(config_data['microphone_index']))

# listen to input
print("Now listening...")
with mic as source:
   audio = r.listen(source)

# print recognized audio
recognized_speech = r.recognize_google(audio)
print(recognized_speech)
speaker.Speak("I got your input")
