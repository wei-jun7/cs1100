# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:46:56 2021

@author: LiWeiJun
"""

def number_happy(sentence):
    sentence1=sentence.lower()
    a=sentence1.count("laugh")
    b=sentence1.count("happiness")
    c=sentence1.count("love")
    d=sentence1.count("excellent")
    e=sentence1.count("good")
    f=sentence1.count("smile")
    return(a+b+c+d+e+f)
#define the function whihc word is happy
def number_sad(sentence):
    sentence1=sentence.lower()
    a=sentence1.count("bad")
    b=sentence1.count("sad")
    c=sentence1.count("terrible")
    d=sentence1.count("horrible")
    e=sentence1.count("problem")
    f=sentence1.count("hate")
    return(a+b+c+d+e+f)
#define the function which word is sad
if __name__=="__main__":
    sentence=input("Enter a sentence => ")
    print(sentence)
    sentence=sentence.lower()
    #ask user to input value and use lower function to make sure no capitial miss
    print('Sentiment: '+"+"*number_happy(sentence)+"-"*number_sad(sentence))
    if number_happy(sentence)==number_sad(sentence):
        print("This is a neutral sentence.")
    elif number_happy(sentence)<number_sad(sentence):
        print("This is a sad sentence.")
    elif number_happy(sentence)>number_sad(sentence):
        print("This is a happy sentence.")
    #use if function to jude the condition and print out the result