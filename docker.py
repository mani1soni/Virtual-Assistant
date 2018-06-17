#!/usr/bin/python3
from fun import tts
import speech_recognition as sr
import os,cv2
from textblob import TextBlob
from textblob.classifiers import NaiveBayesCLassifier
from textblob.classifiers import MaxEntClassifier 
with open('devops.json','r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = (s.getsockname()[0])
s.close()    
class Docker(sr.Recognizer):
    def listen(self, source, timeout = None):

        
        print("starting listening")
        result = super(self.__class__, self).listen(source, timeout)
        print("done listening")
        return result


def docker_clf():
    sr.Recognizer = Docker
    d1 = sr.Recognizer()
    with sr.Microphone(chunk_size = 512) as source:
         audio = d1.listen(source)
    user_input = d1.recognize_google(audio)

    input_data = (user_input)
    output_data = cl.classify(input_data)
    if output_data == 'docker_service_start':
        print (os.system('systemctl start docker'))
    
    elif output_data == 'docker_service_stop':
        print (os.system('systemctl stop docker'))
    
    elif output_data == 'docker_service_restart':
        print (os.system('systemctl restart docker'))
    else :
        tts("try again")
        

        
    
def ml_platform():
    tts("thanks for connecting us")
    tts("please enter your platform name")
    input1 = input("here: ")
    os.system('docker run -itd --name '+input1+'-p 1234:22 ml')
    print ("connect to this ip and port by ssh",ip,":1234")

def website_deploy():
    tts("what kind of style you want you can select from these following")
    img1 = cv2.imread('photos/Autonomy.png',1)
    img2 = cv2.imread('photos/Lambent.png',1)
    img3 = cv2.imread('photos/Pasttime.png',1)
    img4 = cv2.imread('photos/stonework.png',1)
    img5 = cv2.imread('photos/wirework.png',1)
    cv2.imshow('Autonomy',img1)
    cv2.imshow('Lambent',img2)
    cv2.imshow('pasttime',img3)
    cv2.imshow('stonework',img4)
    cv2.imshow('wirework',img5)
    print("press 'q' to quit")
    if waitKey(0) &  0xFF == ord('q'):
        cv2.destroyAllWindows()
    
    menu = '''
             press 1 for Autonomy
             press 2 for Lambent
             press 3 for pasttme
             press 4 for stonework
             press 5 for wirework

            '''
    print(menu)
    input_site = input("enter your choice: ")

    if input_site = 1:
        site = 'Autonomy'
    
    elif input_site = 2:
        site = 'Lambent'
    
    elif input_site = 3:
        site = 'pasttime'

    elif input_site = 4:
        site = 'stonework'
    elif input_site = 5:
        site = 'wirework'

    else:
        tts("may be later")
    tts("enter your container name")
    inp = input("here: ")

    os.system('docker run -itd -v data/:var/www/html -p 9898:80 --name '+inp+'ubuntu:apache2')
    print("enter ip and port in your browser",ip,":9898")

    
        






def docker():
    tts("what do you want to do with docker")
    sr.Recognizer = Docker
    d1 = sr.Recognizer()
    with sr.Microphone(chunk_size = 512) as source:
         audio = d1.listen(source)
    user_input = d1.recognize_google(audio)
   # docker_service = os.system('docker')
   # d = print (docker_service)
   # if d == 0:
    #    os.system('systemctl start docker')

    elif True :
        print("docker service is started")

    if user_input == i:
        print (os.system('docker images')
    elif user_input == c:
        print (os.system('docker run -itd ml'))
    
    elif user_input == cr:
        print (os.system("docker remove `docker ps -qa`"))
        
docker()
