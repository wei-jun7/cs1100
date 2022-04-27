# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 23:47:00 2021

@author: LiWeiJun
"""
'''
This program is use to analysis the sentence and find some important data, such as
ASl,PHW and so on
'''
    
from syllables import find_num_syllables as m
'''
use import to find the syllable of each word in the sentence
'''

def ASL(sentence):
    q=sentence.split()
    x=0
    for i in q:
        if i.count('.')or i.count('!') or i.count('?'):
            x+=1
    return len(q)/x
'''
This program is to find the ASL and use total word divide by sentence to find ASL
'''




def PHW(sentence):
    sentence1=sentence.split()
    sentence2=[]
    for i in sentence1:
        if m(i)>=3:
            sentence2.append(i)
        for j in sentence2:
            
            if j.find('e',len(j)-2)==(len(j)-2)and j.find('s',len(j)-1) ==(len(j)-1):
                sentence2.remove(j)
            elif j.find("d",len(j)-1)==(len(j)-1) and j.find('e',len(j)-2)==(len(j)-2 ):
                sentence2.remove(j)
            elif j.count('-')>0:
                sentence2.remove(j)
    sentence3=len(sentence2)/len(sentence1)*100
    return sentence3

'''
This program si to find the PWH and use the totall number word large than 3 and divide it by totall number of words
'''


def ASYL(sentence):
    sentence4=sentence.split()
    total=0
    for i in sentence4:
        total+=m(i)
    return total/ len(sentence4)
        

'''
This program is to find the ASYL with total syllable divide by total words
'''

    


if __name__ == "__main__":
   sentence=str(input('Enter a paragraph => '))
   '''
   Ask user to input the sentence
   '''
   print(sentence)
   sentence1=sentence.split()
   sentence2=[]
   for i in sentence1:
        if m(i)>=3:
            sentence2.append(i)
        for j in sentence2:
            if j.find('e',len(j)-2)==(len(j)-2)and j.find('s',len(j)-1) ==(len(j)-1):
                sentence2.remove(j)
            elif j.find("d",len(j)-1)==(len(j)-1) and j.find('e',len(j)-2)==(len(j)-2 ):
                sentence2.remove(j)
            elif j.count('-')>0:
                sentence2.remove(j)
   #create the list of hard word
   GFRI = 0.4*(ASL(sentence) + PHW(sentence))
   FKRI=206.835-1.015*ASL(sentence)-86.4*(ASYL(sentence))
   #find teh GFRI and FKRI and print the result out 
   print('Here are the hard words in this paragraph:')
   print(sentence2)
   print('Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}'.format(ASL(sentence),PHW(sentence),ASYL(sentence)))
   print('Readability index (GFRI): {:.2f}'.format(GFRI))
   print('Readability index (FKRI): {:.2f}'.format(FKRI))
    
    
    