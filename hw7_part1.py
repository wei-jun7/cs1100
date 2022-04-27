# -*- coding: utf-8 -*-
"""
This function is use to find the simliar word and correct it which autocorrection base on 
different condition.
"""
'''
This function is use to find the word is in the dictionary and return the string
'''
def FOUND(x):
    if x in list(dictrelative.keys()):
        return 'Found'
    else:
        return 'Not Found'
'''
use list to store the data and drop the each word use the for loop
'''
def DROP(x):
    wordlist=[]
    
    for i in range(len(x)):
        x0=x[0:i]+x[i+1:]
        if x0 in list(dictrelative.keys()) and x0 not in wordlist: 
            wordlist.append(x0)
    return wordlist
'''
use list to store the data and use for loop to examin which letter can be substitution
use if to see in in the data in the dictionary and it should be not repeat
'''
def INSERT(x):
    wordlist=[]
    
    for i in range(len(x)+1):
        for j in list(dictkey.keys()):
            x0=x[0:i]+j+x[i:]   
            if x0 in list(dictrelative.keys()) and x0 not in wordlist: 
                wordlist.append(x0)
    return wordlist
'''
use list to store the data and use for loop to examin which letter can be swap
which the the combination base on the index
use if to see in in the data in the dictionary and it should be not repeat
'''
def SWAP(x):
    wordlist=[]
    
    for i in range(len(x)-1):
        x0=x[0:i]+x[i+1]+x[i]+x[i+2:len(x)]   
        if x0 in list(dictrelative.keys()) and x0 not in wordlist: 
            wordlist.append(x0)
    return wordlist
'''
it is similar to the drop function and add the function to replace it with the 
dictkey
'''
def replace(x):
    wordlist=[]
    
    
    for i in range(len(x)):
        for j in dictkey[x[i]]:
            x0=x[0:i]+j+x[i+1:] 
            if x0 in list(dictrelative.keys()) and x0 not in wordlist: 
                wordlist.append(x0)
    return wordlist



if __name__=='__main__':
#ask user to input and store the data in the dictionary    
    Dfile=input('Dictionary file => ').strip()
    print(Dfile)
    dictrelative=dict()
    for i in open(Dfile):
        word=i.split(',')
        dictrelative[str(word[0])]=str(word[1])
        

            
#ask user to input and store the data in the list         
    Ifile=input('Input file => ').strip()
    print(Ifile)
    filelist=[]
    for i in open(Ifile):

        filelist.append(i.strip())

#ask user to input and store the data in the dictionary        
    Kfile=input('Keyboard file => ').strip()
    print(Kfile)
    dictkey=dict()
    for line in open(Kfile):
        word=line.strip().split(' ')
       
        dictkey[word[0]]=(word[1:])
       
    
    
    
    for i in filelist:
        i=i.strip()
        if FOUND(i)=='Found':
            print( i.rjust(15,' '),'-> FOUND')    #format the output if meet the condition
        else:
             
             possible_way=DROP(i)+INSERT(i)+SWAP(i)+replace(i) #use list to store the result 
             
             possible_word=[]
             for j in possible_way:          #use for loop to find the value in dictrelative and store it in the list
                possible_word.append([str(dictrelative[j]),j])
             possible_word.sort(reverse=True) #sort it base on the relative value and reverse is true
             
             if len(possible_word)==0:
                 print( i.rjust(15,' '),'-> NOT FOUND')#print out the result
             elif 0<len(possible_word)<3:                       
                wordstring=''                            #use string to store the data
                for k in range(len(possible_word)):
                    wordstring=wordstring+' '+possible_word[k][1]     #print out the result     
                    
                
                
                print(i.rjust(15,' '), '-> FOUND',str(len(possible_word)).rjust(2,' ')+ ':',wordstring) #print out the result     
             else:                                                       
                 wordstring=possible_word[0][1]+' '+possible_word[1][1]+' '+possible_word[2][1]          
               
                 print( i.rjust(15,' '), '-> FOUND',str(len(possible_word)).rjust(2,' ')+': ',wordstring)#print out the result     
                
                
                
                
                
                
                