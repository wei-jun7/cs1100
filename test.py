# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:43:01 2021

@author: LiWeiJun
"""

def found(x):                       ###This function is to find whether the word is actually exist in words_10percent.txt
    if relaword.count(x)==1:        ##if it exists, return Found to show it is in that txt
        return 'Found'
    else:                           ##if it not exists, return Unfound to show it is not in that txt
        return 'Unfound'

def drop(x):                        ##this function is to drop one of the letter in the word
    wordpl=[]                       
    i=0
    while i<len(x):                                         ##using while loop to find all the position in this string
        x0=x[0:i]+x[i+1:len(x)]                                 ##drop the letter in that place
        if relaword.count(x0)==1 and wordpl.count(x0)==0:       ##make sure the new words is in words_10percent.txt and have not been found before
                wordpl.append(x0)                           ##add that word in to list
        i=i+1
    return wordpl

def insert(x):                      ##this function is to insert a letter in the word
    wordpl=[]
    i=0
    while i<len(x)+1:                       ##that is nearly the same way to above, but insert one letter from all letters not drop one
        for j in lword:
            x0=x[0:i]+j+x[i:len(x)]        
            if relaword.count(x0)==1 and wordpl.count(x0)==0:       ##make sure the new words is in words_10percent.txt and have not been found before
                wordpl.append(x0)   
        i=i+1
    return wordpl

def swap(x):                        ##this function is to change the place for two letter which are next to each other
    wordpl=[]
    i=0
    while i<len(x)-1:               ##since I will use x[i] and x[i+1], to keep them inrange ,I use len(x)-1
        x0=x[0:i]+x[i+1]+x[i]+x[i+2:len(x)]                         ##that is nearly the same way to above, but change the place for two letters
        if relaword.count(x0)==1 and wordpl.count(x0)==0:       ##make sure the new words is in words_10percent.txt and have not been found before
            wordpl.append(x0)   
        i=i+1
    return wordpl

def replace(x):
    wordpl=[]
    i=0
    x=x.replace(' ','')
    while i<len(x):                                 ##to find all position in this word
        for j in keyboard[x[i]]:                ##pull out all of the possible mistake for this letter from keyboard.txt    (I create a dict for keyboard and letter for keys and maybe-mistakes as values)
            x0=x[0:i]+j+x[i+1:len(x)]           ##replace the new letter to the old
            if relaword.count(x0)==1 and wordpl.count(x0)==0:       ##make sure the new words is in words_10percent.txt and have not been found before
                wordpl.append(x0)   
        i=i+1
    return wordpl

lword=[]
for i in range(97,123):                 ##I found this function on the internet, which is used to output all of the lower letters
    lword.append(chr(i))                ##lword is the list for all of the lower letters

relative=dict()                                 ##create a list called relative
dictname=input('Dictionary file => ')           ##input the name of the original txt file
print(dictname)
f1=open(dictname)                               ##open this file 
content1=f1.read()                              ##read this file              
l0=content1.split('\n')                         ##make a list for each line in the lists of the whole txt
for i in l0:
    if len(i)!=0:
        a=i.split(',')                          ##split the everyline txt in to two parts, word and percent
        relative[a[0]]=(a[1])                   ##words for keys and percent for values
relaword=list(relative.keys())                  ##create a list for keys

inputname=input('Input file => ')       ##input the file name that wants to find possible words
print(inputname)
f3=open(inputname)
words=[]
content3=f3.read()
l2=content3.split('\n')
for i in l2:
    if len(i)!=0:       
        words.append(i)             ##create a list for all of the words in that txt

keyboard=dict()                     ##create another dict for possibile replacement in keyboards.txt
keyb=input('Keyboard file => ')
print(keyb)
f2=open(keyb)
content2=f2.read()
l1=content2.split('\n')
for j in l1:
    if len(j)!=0:
        a=j.split(' ')
        keyboard[a[0]]=(a[1:len(a)])        ##first letter for key and others for values



for i in words:
    i=i.replace(' ','')                         ##using loop to check each sord in list above
    if found(i)=="Found":                   ##if that word exists then print that word is found 
        print('{0:>15} -> FOUND'.format(i))
    else:                                   ##if it is not been found in all possible wor list than using finctions above to find the possible word
        possible=sorted(drop(i)+insert(i)+swap(i)+replace(i))
        print(drop(i),insert(i),swap(i),replace(i))   ##put all of possible words into one list        
        possible_words=[]                           ##create a list called this , which is to put possible words and each possibilities in
        for j in possible:
            possible_words.append([relative[j],j])
            
        possible_words.sort(reverse=True)               ##sorted the list form the most possible word to least
        if len(possible_words)==0:                          ##output of there is no possible word
            print('{0:>15} -> NOT FOUND'.format(i))
        elif 0<len(possible_words)<3:                       ##output of possible words less than 3
            k=0
            wordstring=''
            while k<len(possible_words):
                wordstring=wordstring+' '+possible_words[k][1]          ##make a string to let the output like what is expected
                k=k+1
            wordstring=wordstring.replace('\'','')
            
            print('{0:>15} -> FOUND {1:>2}: {2}'.format(i,len(possible_words),wordstring))
        else:                                                       ##ouput of possible words more than 3
            wordstring=possible_words[0][1]+' '+possible_words[1][1]+' '+possible_words[2][1]           ##make a string for most possible three words           
            wordstring=wordstring.replace('\'','')
            print('{0:>15} -> FOUND {1:>2}:  {2}'.format(i,len(possible_words),wordstring))
            
























