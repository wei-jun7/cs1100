# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:49:59 2021

@author: LiWeiJun
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:16:10 2020
The input word file has two entries per line; the first entry on the line is a single valid word in
the English language and the second entry is a float representing the frequency of the word in the
lexicon. The two values are separated by a comma.
Read this English dictionary into a Python dictionary, using words as keys and frequency as
values. You will use the frequency for deciding the most likely correction when there are multiple
possibilities.
@author: Sijian Tao
"""

def drop(input, dict):
    '''
  If the word is not found, consider all possible ways to drop a single letter from the word.
Store any valid words (words that are in your English dictionary) in some container (list/set/-
dictionary). These will be candidate corrections.

    '''
    drop_dict={}
    for i in range(len(input)):
        if i<len(input)-1:
            str=input[0:i]+input[i+1:]
        elif i==len(input)-1:
            str=input[0:i]
        if str in dict.keys():
            drop_dict[str]=dict.get(str)
    return drop_dict

def insert(input,dict):
    '''
    If the word is not found, consider all possible ways to insert a single letter in the word.
Store any valid words in some container (list/set/dictionary). These will be candidate corrections.
    '''
    insert_dict={}
    for key in dict.keys():
        if len(key)-len(input)==1:
            for i in range(len(key)):
                if i<len(key)-1:
                    str=key[0:i]+key[i+1:]
                elif i==len(key)-1:
                    str=key[0:i]
                if str==input:
                    insert_dict[key]=dict.get(key)
    return insert_dict

def swap(input,dict):
    '''
    Consider all possible ways to swap two consecutive letters from the word. Store any valid
words in some container (list/set/dictionary). These will be candidate corrections.
    '''
    swap_dict={}
    for i in range(len(input)):
        if i+2<=len(input):
            sub=input[i:i+2]
            if input.replace(sub,sub[1]+sub[0]) in dict.keys():
                swap_dict[input.replace(sub,sub[1]+sub[0])]=dict.get(input.replace(sub,sub[1]+sub[0]))
    return swap_dict

def replace(input,dict,keydict):
    '''
    Next consider all possible ways to change a single letter in the word with any other
letter from the possible replacements in the keyboard file. Store any valid words in
some container (list/set/dictionary). These will be candidate corrections.

    '''
    replace_dict={}
    for key in dict.keys():
        if len(key)==len(input):
            for j in range(len(input)):
                if input[j] not in key:
                    for m in keydict.get(input[j]):
                        replace=input[:j]+m+input[j+1:]
                        if replace in dict.keys():
                            replace_dict[replace]=dict.get(replace)
    return replace_dict

if __name__ == "__main__":
    '''
    here is the main part of the code.
    '''

file1=input("Dictionary file => ")
print(file1)
dict_file=open(file1, encoding="utf8").read().splitlines()
dict1=[]
keys=[]
values=[]
for line in dict_file:
    line=line.strip().split(",")
    keys.append(line[0])
    values.append(line[1])
dict1=dict(zip(keys,values))
file2=input("Input file => ")
print(file2)
new=open(file2,encoding="utf8").read().splitlines()
input_file = []
for i in new:
     i = i.strip()
     input_file.append(i)
file3=input("Keyboard file => ")
print(file3)
key_file=open(file3,encoding="utf8").read().splitlines()
key=[]
value=[]
for li in key_file:
    li=li.strip().split(" ")
    key.append(li[0])
    value.append(li[1:])
dict_keyboard=dict(zip(key,value))

for input in input_file:
    final_dict ={}
    if input in dict1.keys():
        print('{:>15} -> FOUND'.format(input))
    elif input not in dict1.keys():
        if len(drop(input,dict1)) !=0:
            final_dict.update(drop(input,dict1))
        if len(insert(input,dict1)) !=0:
            final_dict.update(insert(input,dict1))
        if len(swap(input,dict1))!=0 :
            final_dict.update(swap(input,dict1))
        if len(replace(input,dict1,dict_keyboard))!=0:
            final_dict.update(replace(input,dict1,dict_keyboard))


        final_list=[(final_dict[x],x) for x in final_dict.keys()]
        final_list.sort(reverse=True)
        final_li=[final_list[i][1] for i in range(len(final_list))]
        if len(final_dict)!=0 and len(final_li)<=3:
            print('{0:>15} -> FOUND {1:>2}: '.format(input,str(len(final_li))),*final_li)
        elif len(final_dict)!=0 and len(final_li)>3:
            print('{0:>15} -> FOUND {1:>2}: '.format(input,str(len(final_li))),*[final_li[0],final_li[1],final_li[2]])
        else:
            print('{:>15} -> NOT FOUND'.format(input))