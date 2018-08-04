import sys

def speak(words):
  if sys.platform in ['Windows', 'win32', 'cygwin']:
      import win32com.client
      
      # create speaker
      speaker = win32com.client.Dispatch("SAPI.SpVoice")
      speaker.Speak(words)
  