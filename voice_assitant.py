import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import pyautogui

engine = pyttsx3.init()


def speak(text):
  print('[Jarvis] : ' +text)
  engine.say(text)
  engine.runAndWait()
  
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\arbaz\\Desktop\\Open-cv\\jarvis\\ss.png")
    
def jokes():
    speak(pyjokes.get_joke())

  
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wish_me():
  speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")

    speak("Jarvis at your service. Please tell me how can i help you?")

def takeCommand():
  #It takes microphone input from the user and returns string output
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")    
    command = r.recognize_google(audio, language='en-in')
    print('[Me]:' +command)

  except Exception as e:
    # print(e)    
    return "None"
  return command

# script starts here

wish_me()
while True:
# if 1:
  command = takeCommand().lower()

  # Logic for executing tasks based on command
  command = command.replace('jarvis', '')

  if 'wikipedia' in command:
    speak('Searching Wikipedia...')
    command = command.replace("wikipedia", "")
    command = command.replace("search", "")
    command = command.replace("for", "")
    results = wikipedia.summary(command, sentences=1)
    speak('According to wikipedia, ' +results)

  elif 'open youtube' in command:
    speak('Opening Youtube')
    webbrowser.open("https://youtube.com")

  elif 'open google' in command:
    speak('Opening Google')
    webbrowser.open("https://google.com")

  elif 'open stack overflow' in command:
    speak('Opening StackOverflow')
    webbrowser.open("https://stackoverflow.com")

  elif 'what' in command and 'time' in command:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak('Sir, The time is ' +strTime)

  elif 'meaning of life' in command:
    speak('Sir, the meaning of life is 42.')
  
  elif 'how are you' in command:
    speak('I am doing jolly good, sir.')

  elif 'bye' or 'thank you' in command:
    speak('Goodbye, Have a nice day!')
    
  elif 'joke' in query:
		jokes()
     
  elif 'screenshot' in query:
		 screenshot()
		 speak("Done!")
      
  else:
    speak('I didn\'t quiet catch you sir. Can you please try that again?')
    

