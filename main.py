import speech_recognition as sr
import json
import os
import sys
import win32com.client
import winsound
import decoder

def beep():
    frequency = 1200  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def listen_for_input(r, mic):
    # listen to input
    print("Now listening...")
    beep()

    with mic as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # try to recognize audio

    try:
        recognized_speech = r.recognize_google(audio)
        print(recognized_speech)
        decoder.decode(recognized_speech.lower())
        
        listen_for_input(r, mic)
    except sr.RequestError:
        # API was unreachable or unresponsive
        print("There was an error: API unavailable")
    except sr.UnknownValueError:
        # speech was unintelligible
        print("There was an error: Unable to recognize speech")
        speaker.Speak("Sorry, I didn't get that.")
        listen_for_input(r, mic)

if __name__ == "__main__":
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
        config_data["microphone_index"] = mic_choice

        # then create config file
        # and write mic choice to it
        with open(config_file, 'w') as outfile:
            json.dump(config_data, outfile)

    # declare mic to use
    mic = sr.Microphone(device_index=int(config_data["microphone_index"]))

    listen_for_input(r, mic)
