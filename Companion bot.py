#!/usr/bin/env python
# coding: utf-8

# In[1]:


##pip install wolframalpha


# In[2]:


##pip install pyttsx3


# In[3]:


##pip install wikipedia


# In[4]:


##pip install SpeechRecognition


# In[5]:


##pip install ecapture


# In[6]:


##pip install pyjokes


# In[7]:


##pip install twilio


# In[8]:


##pip install requests 


# In[9]:


##pip install beautifulsoup4


# In[10]:


##pip install pyaudio


# In[11]:


##pip install ipynb


# In[ ]:





# In[1]:


import recipe_function
from recipe_function import recipe_search
from recipe_function import f1
from recipe_function import f2
from recipe_function import f3
from recipe_function import f4
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pandas as pd 
import numpy as  np 
import pyaudio
import pyjokes

import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client

from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


# In[2]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# In[3]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening!") 
  
    assname =("companionBot 1 point o")
    speak("I am your Assistant")
    speak(assname)
     
 
def username():
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome companion", uname.center(columns))
    print("#####################".center(columns))
     
    
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        
        print("Please respond") 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Please wait, Interpreting your requierment...")
        #print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

def recipe():
    global f
    global f2
    speak("Which recipie do you want")
    Recipie = takeCommand().lower()
    recipe_search(Recipie)
    #if f!=-1:
     #   speak("Here are the ingredients you need:")
      #  print("Here are the ingredients you need")
    f1()
    #if f2!=-1:   
    #speak("Steps for the recipe")
    #print("Steps for the recipe")
    f3()
    
    
    


  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


# In[12]:


if __name__ == '__main__':
    clear = lambda:os.system('cls')
     
    
    clear()
    wishMe()
    username()
    recipe()
    h = 0
    while h!= -1:
        
        speak('Do you want to continue?')
        print('Do you want to continue?')
        cont = takeCommand().lower()
        if cont == 'no':
            h = -1
        elif cont ==  'yes':
            h = 0
            recipe()
        else :
            speak("Can you please repeat")
            print("Can you please repeat")
            
     
    while False:
         
        query = takeCommand().lower()
        
        
         
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open recipe world' in query:
            speak("Here you go to recipe world")
            webbrowser.open("gorecipeworld.com")  
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")
 
        elif 'open opera' in query:
            codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)
 
        elif 'email to harshil' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Gaurav.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
             
        elif "calculate" in query:
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Gaurav. further It's a secret")
 
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Gaurav ")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")
 
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop companionBot from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "companionBot Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('companionBot.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("companionBot.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
                     
       
        elif "companionBot" in query:
             
            wishMe()
            speak("Companion BOt 1 point o in your service Mister")
            speak(assname)
 
             
        elif "send message " in query:
                
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
       
        elif "will you be my friend" in query or "will you be my best friend" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "what is" in query or "who is" in query:
             
           
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
        
       ## elif 'Recipie' in query:
             # Recipie = takeCommand()
              #speak(Recipie)
              #print(Recipie)+ 
                
            
            
            
            ##for i in range(0,len(ingredients)):
                ##speak(ingredients[i])
                


# In[ ]:


# paused paused 
# convert input nums in int form
# assign step no. to recipe steps such that any no of step can be called when asked to repeat
# ingredients display
# do not execute f3 function when stop command is issued for ing


# #### while false kiya hai.... to execute wikipidea n all usko true ke dena

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




