# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:44:25 2020

@author: DeepanwitaDatta

There are two players in the game. One will think of a word, jumble it and present it to the other. 
The other needs to guess that. The turns will be alternated. The questions will be posted by the 
computer to avoid bias. The answers will be given by the players
"""

import random

def choose():
    words=["PROGRAMMING","SPLUNK","TABLEAU", "HADOOP", "PYTHON", "NUMPY", "SCIPY","REGRESSION",
           "STATISTICS", "PROVISIONING","KAFKA","DBLOADER","DEVOPS","MATHEMATICS","REVERSE","RAINBOW",
           "PROCEDURES","TRIGGERS","FUNCTIONS","VIEWS","KUBERNETES","DOCKER","CONTAINER"]
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return(jumbled)
    
def thank(P1n,P2n,p1,p2):
    print(P1n," your score is: ",p1)
    print(P2n," your score is: ",p2)
    print("Thank you for your participation. Hope to see you soon!!!")
    
def play():
    P1name=input("Player 1, please input your name ")
    P2name=input("Player 2, please input your name ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #Computer's task
        picked_word=choose()
        #Create the Question
        qn=jumble(picked_word)
        print(qn)
        #Player 1
        if turn%2==0:
            print(P1name," it is your turn")
            ans=input("What is on my mind? ")
            if ans==picked_word:
                pp1=pp1+1
                print("Your score is: ",pp1)
            else:
                print("Better Luck next time. I thought:", picked_word)
            c=input("Press 1 to continue or 0 to quit: ")    
            c=int(c)
            if(c==0):
                thank(P1name,P2name,pp1,pp2)
                break
        #Player 2
        else:
            print(P2name," it is your turn")
            ans=input("What is on my mind? ")
            if ans==picked_word:
                pp2=pp2+1
                print("Your score is: ",pp2)
            else:
                print("Better Luck next time. I thought:", picked_word)
            c=input("Press 1 to continue or 0 to quit: ")
            c=int(c)
            if(c==0):
                thank(P1name,P2name,pp1,pp2)
                break
        turn=turn+1
        
play()