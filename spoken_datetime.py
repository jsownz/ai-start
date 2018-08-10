def getSpokenTime(hour,minute):
  hours = ["twelve","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","one","two","three","four","five","six","seven","eight","nine","ten","eleven"]
  minutes = ["","one","two","three","four","five","six","seven","eight","nine"]
  spokenHour = hours[hour]

  firstDigit = int(minute[0])
  secondDigit = int(minute[1])
  prefix = ""
  suffix = ""
  if (firstDigit == 0):
    if (secondDigit != 0):
      prefix = "oh"
      suffix = minutes[secondDigit]
  elif (firstDigit == 1):
    if (secondDigit == 0):
      suffix = "ten"
    elif (secondDigit == 1):
      suffix = "eleven"
    elif (secondDigit == 2):
      suffix = "twelve"
    elif (secondDigit == 3):
      suffix = "thirteen"
    elif (secondDigit == 4):
      suffix = "fourteen"
    elif (secondDigit == 5):
      suffix = "fifteen"
    elif (secondDigit == 6):
      suffix = "sixteen"
    elif (secondDigit == 7):
      suffix = "seventeen"
    elif (secondDigit == 8):
      suffix = "eighteen"
    elif (secondDigit == 9):
      suffix = "nineteen"
  elif (firstDigit == 2):
    prefix = "twenty"
    suffix = minutes[secondDigit]
  elif (firstDigit == 3):
    prefix = "thirty"
    suffix = minutes[secondDigit]
  elif (firstDigit == 4):
    prefix = "forty"
    suffix = minutes[secondDigit]
  elif (firstDigit == 5):
    prefix = "fifty"
    suffix = minutes[secondDigit]

  spokenMinute = "{} {}".format(prefix, suffix)

  spokenTime = "{} {}".format(spokenHour, spokenMinute)

  return spokenTime