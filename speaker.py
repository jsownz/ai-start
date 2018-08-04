import sys

def speak(words):
  if sys.platform in ['Windows', 'win32', 'cygwin']:
      import win32com.client

      # create speaker
      speaker = win32com.client.Dispatch("SAPI.SpVoice")
      speaker.Speak(words)
  elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    from os import system
    system("say %s" % words)

  elif sys.platform in ['linux', 'linux2']:
    print("Not implemented yet")