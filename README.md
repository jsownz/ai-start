## Need to install a few pip packages for it to work:

```
pip install SpeechRecognition
pip install PyAudio
```

Not sure how the talking back will work on non-windows systems yet and in the process of trying differnt TTS packages, I don't know if the current code will work without a pip package or not. May need pypiwin32 or pywin32

## Notes
- After a few translations it's getting hung up... I'm not sure what's causing this yet. Doesn't appear to be a memory leak, but I need to dig further to see what's happening here.
- Would like to work on adding extensions - here's some ideas:
    - open virtual machines
    - add calendar events
    - cross-reference some data (parse then google terms and show results?)
    - open email client
    - spawn a web service of some sort
    - get the owner of a domain from whois
    - get an ip address from nslookup and copy to keyboard
    - check if site is up
    - ssh to a machine
    - run a portscan on an ip address or domain and report relevant results
    - get the weather
    - send this to my phone (get active window, decide what it is and how to send it [text, companion app, etc])
    - whatever else