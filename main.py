import speech_recognition as sr
import json
import os
import sys
import decoder
import config
import speaker

def beep():
    frequency = 1200  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        import winsound
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
        speaker.speak("Sorry, I didn't get that.")
        listen_for_input(r, mic)

if __name__ == "__main__":
    # set config data
    config_data = config.get_config()
    # declare recognizer
    r = sr.Recognizer()

    try:
        mic_choice = config_data["microphone_index"]
    except KeyError:
        # didnt find a microphone index, get mic selection
        print("No config file found. Please select a microphone to use")
        print("-------------------------------------------------------")
        # loop over mic options and print them out nicely
        for index,choice in enumerate(sr.Microphone.list_microphone_names()):
            print("%s - %s" % (index,choice))
        
        # get user mic choice
        mic_choice = int(input("Select the index of the mic: "))

        # save microphone index
        config.save_config("microphone_index",mic_choice)

    # declare mic to use
    mic = sr.Microphone(device_index=int(mic_choice))

    listen_for_input(r, mic)
