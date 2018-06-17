#!/usr/bin/python3
import speech_recognition as sr
import os,time,datetime,cv2,pyttsx3,urllib,urllib.parse,pafy,webbrowser
from bs4 import BeautifulSoup
from textblob import TextBlob
from nltk.corpus import wordnet
import numpy as np
from textblob.classifiers import NaiveBayesClassifier
with open('document.json','r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")



engine = pyttsx3.init()


    
def tts(voice_input_data):
    engine = pyttsx3.init()
   # voices = engine.getProperty('voices')
   # engine.setProperty('voice', voices[1].id)
    engine.say(voice_input_data)
    engine.runAndWait()



def camera():
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    img_counter = 0
    cam = cv2.VideoCapture(0)
    print("hit 'space' to click a pic\n hit 'Esc' to quit")

    while True:
        
         ret, frame = cam.read()
         cv2.imshow("test", frame)
         if not ret:
             break
         k = cv2.waitKey(1)

         if k%256 == 27:
             # ESC pressed
             print("Escape hit, closing...")
             break
         elif k%256 == 32:
             # SPACE pressed
             img_name = ("/home/manish/Desktop/"+date+"opencv_frame_{}.png".format(img_counter))

             cv2.imwrite(img_name, frame)
             print("{} written!".format(img_name))
             img_counter += 1
    
    cam.release()

    cv2.destroyAllWindows()






class WordDef(sr.Recognizer):
    def listen(self, source, timeout = None):
        print("starting listening")
        result = super(self.__class__, self).listen(source, timeout)
        print("done listening")
        return result


class VideoPlay(sr.Recognizer):
    def listen(self, source, timeout = None):
        print("starting listening")
        result = super(self.__class__, self).listen(source, timeout)
        print("done listening")
        return result



def Video_Search():
    #engine.say("what video you want to search")
    #engine.runAndWait()
    tts("what video you want to play")
    sr.Recognizer = VideoPlay
    sa = sr.Recognizer()
    with sr.Microphone(chunk_size = 512) as source:
         audio = sa.listen(source)
    srch_query = sa.recognize_google(audio)
   
    
    
    query = urllib.parse.quote(srch_query)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)

    html = response.read()

    soup = BeautifulSoup(html)
    zx = 0
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):

        x = ('https://youtube.com/'+vid['href'])
        print (zx)

        if x !=None and zx ==1:

             recv_url = x
             break

        zx += 1
    
    


    video = pafy.new(recv_url)
    best = video.getbest()
    playurl = best.url
    webbrowser.open(playurl)
   
   

class Search(sr.Recognizer):
    def listen(self, source, timeout = None):

        
        print("starting listening")
        result = super(self.__class__, self).listen(source, timeout)
        print("done listening")
        return result

def Search_Anything():
    #engine.say("what do you want to search")
    #engine.runAndWait()
    tts("what do you want to search")
    sr.Recognizer = Search
    sa = sr.Recognizer()
    with sr.Microphone(chunk_size = 512) as source:
         audio = sa.listen(source)
    user_input = sa.recognize_google(audio)
    result = webbrowser.open("https://www.google.com/search?q="+user_input)
    



    


class SentAnalyzer(sr.Recognizer):
    def listen(self, source, timeout = None):
        print("starting listening")
        result = super(self.__class__, self).listen(source, timeout)
        print("done listening")
        return result

def sentiment_Analyzer():
    #engine.say("Speak a sentence")
    #engine.runAndWait()
    tts("Speak a sentence")
    sr.Recognizer = SentAnalyzer
    sa = sr.Recognizer()
    with sr.Microphone(chunk_size = 512) as source:
         audio = sa.listen(source)
    user_input = sa.recognize_google(audio)

    
    analysis = TextBlob(user_input)
    print(analysis.sentiment)
    if analysis.sentiment.polarity == 0:
        engine.say("your sentiment is nutral")
        engine.runAndWait()
    elif analysis.sentiment.polarity > 0:
        engine.say("your sentiment is positive")
        engine.runAndWait()

    elif analysis.sentiment.polarity < 0:
        engine.say("your sentiment is negative")
        engine.runAndWait()
    

def word_def_ex():
    #engine.say("speak a word")
    #engine.runAndWait()
    tts("speak a word")
    sr.Recognizer = WordDef
    w = sr.Recognizer()
    with sr.Microphone(chunk_size = 512) as source:
         audio = w.listen(source)
    user_input1 = w.recognize_google(audio)
    result = wordnet.synsets(user_input1)
    re = (result[0].definition())
    tts(re)
    print(re)

    print(result[0].examples())





def bot_help():
    print("__camera()__   ---\n say 'take picture' for open camera\n press 'space' for clicking picture\n press 'Esc' for quit...\n")

    print("\n__sentiment_Analysis()__ ---\n say 'analysis' for sentiment analysis\n")

    print("\n__word_def_ex()__ ---\n say 'definition' for asking word's definition\n")

    print("\n__Video_Search()__ ---\n say 'video' for search for a video\n")

    print("\n__Search_Anything()__ ---\n say 'search' for search anything\n")






