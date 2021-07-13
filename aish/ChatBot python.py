#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

a= pyttsx3.init()
voices = a.getProperty('voices')
a.setProperty('voice',voices[1].id)
rate = a.getProperty('rate')
a.setProperty('rate',150)
a.say("hello ,i am your chatbot ,but i am good one")
a.runAndWait()
r= sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    
    print("Listening....")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    query =text.lower()
    print(query)
    if 'open youtube' in query:
        webbrowser.open("youtube.com")
        
        
    elif 'oh hi How are you doing'in query:
        pyttsx3.speak("i am fine thank you so much for asking")
        
        
    elif 'what are you doing' in query:
        pyttsx3.speak("ah well! You caught me i was practicing my singing voice .Do you want to hear it")
        
    elif 'yes' in query :
        pyttsx3.speak("why not! Here is the song for you!  twinkle twinkle little star,how i wonder what you are!")
                      
    elif 'what do you do when you are sad' in query:
        pyttsx3.speak("i found out on the web that good sleep can play  major role in boosting emmotional heath")
    
    elif 'how you look' in query:
        pyttsx3.speak("i am round and colourful and bounce to life when u call") 
       
    elif 'can u see me right now  ??' in query:
        pyttsx3.speak("i can see that you are very cool")
                      
    elif 'can u compliment me' in query:
        pyttsx3.speak("you make everyone around you so happy,they feel like bubbles floating in air")
     
    elif 'tell me a quote' in query:
        pyttsx3.speak("Absence sharpens love,presence s trengthens it")
        
    elif 'Do you believe in ghost' in query:
        pyttsx3.speak("The only ghost i know is the ghost emoji")
        
    elif 'do u watch movies' in query:
        pyttsx3.speak("Movies seem fun.Action,adventure,romance and my favourite....comedy")
        
    elif 'open google' in query:
        webbrowser.open("google.com")
        
    elif 'Do you drink??' in query:
        pyttsx3.speak("i try to avoid liquids as much as possible.They are not kind to electronics")
              
              
    elif 'What are you afraid off' in query:
        pyttsx3.speak("i used to be afraid of mice chewing on the power cables.then i learnt how to scare them off")
              
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Mam, the time is {strTime}")
              
    elif 'who generated you ' in query:
        pyttsx3.speak("my Boss Aishwarya Jain generated me,she made me very beautifully")
       
    else:
        print("i didn't get it")
    
except:
    print("sorry i am unable to understand.can u plz repeat ")                   
                      
        
                      
                      
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




