#!/usr/bin/python3
import speech_recognition as sr
from nltk.corpus import wordnet
import pyttsx3,os,time,datetime,cv2,urllib,urllib.parse,pafy,webbrowser
from textblob import TextBlob
import numpy as np
from textblob.classifiers import NaiveBayesClassifier
with open('document.json','r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")
from fun import tts
from fun import sentiment_Analyzer
from fun import camera
from fun import word_def_ex
from fun import Video_Search
from fun import Search_Anything
from fun import bot_help

engine = pyttsx3.init()
g=('greetings')
x=('photo')
y=('sentiment_analysis')
z=('word_definition')
p=('video')
s=('search')
h=('help')
q=('quit')


class CustomSource(sr.Microphone):
    def init(self, device_index = None, sample_rate = 16000, chunk_size = 1024):
        print("about to initialize microphone")
        result = super(self.__class__, self).init()
        print("done initializing microphone")
        return result

class CustomRecognizer(sr.Recognizer):
    def listen(self, source, timeout = 20):
       # print ("instructions!!! \n")
        time.sleep(0.6)
       # print ("say 'take picture' for clicking a picture")
       # print("say 'analysis' for sentence analysis")
       # print ("say 'definition' for word's definition")
       # print ("say 'video' for playing video")
       # print("say 'search' for search anything")
       # print("OR....")
       #	print("speak a valid command \n !!Caution expert pronunciation Required ")
       # time.sleep(1)
       	print("starting listening")
       	result = super(self.__class__, self).listen(source, timeout)
       	print("done listening")
       	
        return result
sr.Recognizer = CustomRecognizer
sr.Microphone = CustomSource


while True:
   

   
    while True:
        try:


            r = sr.Recognizer()
            with sr.Microphone(chunk_size = 512) as source:
                audio = r.listen(source)
            user_input_command = r.recognize_google(audio)
            print(user_input_command)
            if user_input_command == 'hello':
                break
        except:
            continue

    try:
        r = sr.Recognizer()
        with sr.Microphone(chunk_size = 512) as source:
            audio = r.listen(source)
        user_input_command = r.recognize_google(audio)
        output = cl.classify(user_input_command)
        if output == g:
            engine.say("hii, i am your personal assistent")
            engine.runAndWait()
             
        elif output == x:

            print ("press q to click")
            print("Camera is about to  open!!!!!")
            time.sleep(1)
            camera()
        
        
    
        elif output :
            sentiment_Analyzer()
        
        elif output == z:
            word_def_ex()
        
        elif output == p:
            Video_Search()
        elif output == s:
            Search_Anything()
    
        elif output == h:
            bot_help()
        elif output == q:
            break
                  
        else:                
            print ('nothing')
        
            y=os.system(user_input_command)
            print (y)
            #print("you said:  " + r.recognize_google(audio))
     
    except:
            os.system('echo " this is not a command,try again" | festival --tts')

