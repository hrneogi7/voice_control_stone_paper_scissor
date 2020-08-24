# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:24:56 2020

@author: RITTWICK
"""

import speech_recognition as sr
from gtts import gTTS
import random
import playsound
import os
#import time
class player:
    name=''
    def playername(self,name):
        self.name=name
class hrit:
    name=''
    def selfname(self,name):
        self.name=name
r=sr.Recognizer()
def listenit(ask=""):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source, 5, 5)  
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  
        except sr.UnknownValueError: 
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') 
        print(">>", voice_data.lower()) 
        return voice_data.lower()
def speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) 
    playsound.playsound(audio_file) 
    print(hrit_obj.name + ":", audio_string) 
    os.remove(audio_file)
def play():
    #speak("Say stop when want to end the game")
    
    player=0
    comp=0
    p=True
    while p==True:
        voice_data = listenit("choose among rock  paper  scissor to play or say finish to end the game")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        if pmove=="finish":
            p==False
            break
        
    
        #speak("The computer chose " + cmove)
        #speak("You chose " + pmove)
        
        if pmove==cmove:
            speak("The computer chose " + cmove)
            speak("drawn attempt")
        elif pmove== "rock" and cmove== "scissor":
            speak("The computer chose " + cmove)
            speak("You wins this turn")
            player+=1
        elif pmove== "rock" and cmove== "paper":
            speak("The computer chose " + cmove)
            speak("oops computer wins this")
            comp+=1
        elif pmove== "paper" and cmove== "rock":
            speak("The computer chose " + cmove)
            speak("great going keep it up")
            player+=1
        elif pmove== "paper" and cmove== "scissor":
            speak("The computer chose " + cmove)
            speak("oops next time")
            comp+=1
        elif pmove== "scissor" and cmove== "paper":
            speak("The computer chose " + cmove)
            speak("you win")
            player+=1
        elif pmove== "scissor" and cmove== "rock":
            speak("The computer chose " + cmove)
            speak("i won this time")
            comp+=1
        
        
    l=[0,0]
    if comp>player:
        speak(player_obj.name+"You lose better luck next time")
        l[0]=player
        l[1]=comp
        return l
    elif player>comp:
        speak("Congrats mister "+player_obj.name+" you won")
        l[0]=player
        l[1]=comp
        return l
        
    else:
        speak("match drawn")
        l[0]=player
        l[1]=comp
        return l
    
#time.sleep(1)
player_obj=player()
hrit_obj=hrit()
hrit_obj.name='Rexa'
speak("hello, welcome to new game of stone paper scissor")
name1=listenit("What is your name?")
player_obj.name=name1
speak("Hi "+player_obj.name+" my name is  "+hrit_obj.name)
c=listenit("Arey you ready for the game?")
if c.lower()=="yes":   
    while(1):
        voice_data = listenit("Say play to begin") 
        #print("Done")
        
        if voice_data=="play":
            
            c=play()
            print(player_obj.name+" score: ",c[0])
            print(hrit_obj.name+" score: ",c[1])
        else:
            exit()
else:
    speak("ok comeback later")
    exit()
