# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:49:32 2021

@author: LiWeiJun
"""
#import the moduel we want 
import hw4_util
#find the lenght of function and give the score
def test_length(x):
    score=0
    if 6<=len(x)<=7:
        score+=1
        print('Length: +1')
    elif 8<=len(x)<=10:
        score+=2
        print('Length: +2')
    elif len(x)>10:
        score+=3
        print('Length: +3')
    return score
#find the case of function and give the score
def test_case(x):
    score1=0
    z=0
    y=0
    for i in x:
        if i.isupper():
            z+=1
        elif i.islower():
            y+=1
    if y==1 or z==1:
        score1=1
        print('Cases: +1')
    elif y>=2 and z>=2:
        print('Cases: +2')
        score1=2
    return score1
#find the digits of function and give the score
def test_digits(x):
    score2=0
    for i in x:
        if i.isdigit():
            score2+=1
    if score2==1:
        print('Digits: +1')
    elif score2>=2:
        print('Digits: +2')
        score2=2
    return score2
#find the punction of function and give the score
def test_punctuation(x):
    punt1='!@#$'
    punt2='%^&*'
    score3=0
    for i in x:
        if punt1.find(i)>=0:
            score3+=1
            print('!@#$: +1')
            break
        elif punt2.find(i)>=0:
            score3+=1
            print('%^&*: +1')
            break

    if score3>=2:
        score3=2
    return score3
#find the word compare with licenes of function and give the score
def test_NY(x):
    score4=0
    
    for i in range(len(x)-6):
        if x[i].isalpha() and x[i+1].isalpha() and x[i+2].isalpha() and x[i+3].isdigit() and x[i+4].isdigit() and x[i+5].isdigit() and x[i+6].isdigit():
            score4=-2
            print('License: -2')
    return score4 
#find the word compare with common password list of function and give the score
def test_common(x):
    x=x.lower()
    score5=0
    u=hw4_util.part1_get_top()
    if str(u).find(x)>=0:
        print('Common: -3')
        score5-= 3
    return score5

#ask user to input the passwork
if __name__ == '__main__':
    x=input('Enter a password => ').strip()
    print(x)
    combin=0
    
    #calculation the number of totoal score
    
    combin=test_length(x)+test_case(x)+test_digits(x)+test_punctuation(x)+test_NY(x)+test_common(x)
    #use different condition to rate the password and print the value we want 
    print('Combined score:',combin)
    if combin<=0:
        print('Password is rejected')
    elif 1<=combin<=2:
        print('Password is poor')
    elif 3<=combin<=4:
        print('Password is fair')
    elif 5<=combin<=6:
        print('Password is good')
    elif combin>=7:
        print('Password is excellent')        
            
        
        
        
        
        
        
        
        
        




