# -*- coding: utf-8 -*-
"""
This function is use to compare two text file and find the similarity and different between two file
"""
'''
this function is use to conver the file be the list and remove teh repeat one and empty one
'''
def make_list(x):
    file=open(x,encoding='UTF-8')
    total=list()
    for i in file:
        line=i.lower().strip().split()
        for j in line:
            for k in j:
                if  not k.isalpha():
                    j=j.replace(k,'')
            total.append(j)
            for l in total:
                if l =='':
                    total.remove(l)
    
    return total            
'''
This function is store word the same length keys and find the store max lenght in a variable, then print out the 
result in some format base on the len of word which store in the string in to print out
'''                    
                
def prase_line(x):
    dictionx=dict()
    for m in x:
        
        length=str(len(m))
        
        if length in dictionx:
            dictionx[length].add(str((m)))
        else:
            dictionx[length]=set()
            dictionx[length].add(str((m)))
    
    
    init=0
    for v in list(dictionx.keys()):
        if int(v)>int(init):
            init=int(v)
    
    
         
    for num in range(1,init+1):
        if num<10:
            if str(num) in list(dictionx.keys()):
                value=''
                listt=[]
                listt.append(sorted(dictionx[str(num)]))
                
                for d in sorted(dictionx[str(num)]):
                    
                    
                    if len(dictionx[str(num)])<=6:
                        value+=d+' '
    
                        
                if len(dictionx[str(num)])>6 and len(listt[0])>=6:
                    
                    value+=str(listt[0][0])+' '+str(listt[0][1])+' '+str(listt[0][2])+' ... '+str(listt[0][-3])+' '+str(listt[0][-2])+' '+str(listt[0][-1])
                if len(str(len(dictionx[str(num)]))) >=2:
                    print('   '+str(num)+': ',str(len(dictionx[str(num)]))+':', value.strip())
                else:
                    print('   '+str(num)+':  ',str(len(dictionx[str(num)]))+':', value.strip())
            else:
                print('   '+str(num)+':  ',str(0)+':')
        if num>=10:
            if str(num) in list(dictionx.keys()):
                value=''
                listt=[]
                listt.append(sorted(dictionx[str(num)]))
                
                for d in sorted(dictionx[str(num)]):
                    
                    
                    if len(dictionx[str(num)])<=6:
                        value+=d+' '
    
                        
                if len(dictionx[str(num)])>6 and len(listt[0])>=6:
                     value+=str(listt[0][0])+' '+str(listt[0][1])+' '+str(listt[0][2])+' ... '+str(listt[0][-3])+' '+str(listt[0][-2])+' '+str(listt[0][-1])
                if len(str(len(dictionx[str(num)]))) >=2:
                    print('  '+str(num)+': ',str(len(dictionx[str(num)]))+':', value.strip())
                else:
                    print('  '+str(num)+':  ',str(len(dictionx[str(num)]))+':', value.strip())
            else:
                print('  '+str(num)+':  ',str(0)+':')
    return dictionx
'''
This funtion is find the distinct_pair which base on the max_sep and store the list also, we store the a list have
repeat distinct pair list which is pair0
'''
def distinct_pair(x,y):
    i=0
    pair0=[]
    pair1=[]
    for i in range(len(x)):
        index=min(i+y,len(x))
        l=x[i:index+1]
        for j in range(1,len(l)):
            pair0.append(sorted([l[0],l[j]]))

    pair0=sorted(pair0)
    
    for i in pair0:
        if 0 == pair1.count(i) and i  not in pair1 :
            pair1.append(i)
    return [pair0, pair1]
    
    
    
    
    
    
    
'''
ask the user to input the data and print out.
'''

file1=input('Enter the first file to analyze and compare ==> ')
print(file1)
f1=str(file1)

file2=input('Enter the second file to analyze and compare ==> ')
print(file2)
f2=str(file2)

number=int(input('Enter the maximum separation between words in a pair ==> '))
print(number)
print()


print('Evaluating document',file1)
#use the function to get the list and store in the variable
x=make_list(file1)
y=make_list(file2)

file3='stop.txt'
stop_word=make_list(file3)
stop_word=set(stop_word)
#this one is compare two list with stop.txt and remove the repeat one
for word in stop_word:
    while 0!= x.count(word):
        x.remove(word)
    while 0!= y.count(word):
        y.remove(word)

length_y=0
length_x=0
#find the len of total word in the txt
for words in y:
    length_y+=len(words)

        

for wordss in x:
    length_x+=len(wordss)
#find the average len of fiel and use set to remove the repeat one
average_x=length_x/len(x)
average_y=length_y/len(y)
a=set(x)
b=set(y)
ratiox=len(a)/len(x)
ratioy=len(b)/len(y)
print('1. Average word length: {:.2f}'.format(average_x))
print('2. Ratio of distinct words to total words: {:.3f}'.format(ratiox))
print('3. Word sets for document',file1+':')
prase_line(x)
print('4. Word pairs for document',file1)
#call the funtion 
pair101=distinct_pair(x,number)[0]
pair102=distinct_pair(x,number)[1] 
print('  {0} distinct pairs'.format(len(pair102)))
if len(pair102)<=10:#print out the result in some formate
    for i in pair102:
        print('  {0} {1}'.format(i[0],i[1]))
else:
    print('  {0} {1}'.format(pair102[0][0],pair102[0][1]))
    print('  {0} {1}'.format(pair102[1][0],pair102[1][1]))
    print('  {0} {1}'.format(pair102[2][0],pair102[2][1]))
    print('  {0} {1}'.format(pair102[3][0],pair102[3][1]))
    print('  {0} {1}'.format(pair102[4][0],pair102[4][1]))
    print('  ...')
    print('  {0} {1}'.format(pair102[-5][0],pair102[-5][1]))
    print('  {0} {1}'.format(pair102[-4][0],pair102[-4][1]))
    print('  {0} {1}'.format(pair102[-3][0],pair102[-3][1]))
    print('  {0} {1}'.format(pair102[-2][0],pair102[-2][1]))
    print('  {0} {1}'.format(pair102[-1][0],pair102[-1][1]))
print('5. Ratio of distinct word pairs to total: {0:.3f}'.format(len(pair102)/len(pair101)))
#print the the requirment
print()
print('Evaluating document',file2)
print('1. Average word length: {:.2f}'.format(average_y))
print('2. Ratio of distinct words to total words: {:.3f}'.format(ratioy))
print('3. Word sets for document',file2+':')
prase_line(y)
print('4. Word pairs for document',file2)
#call the funtion 
pair201=distinct_pair(y,number)[0]
pair202=distinct_pair(y,number)[1]

print('  {0} distinct pairs'.format(len(pair202)))
if len(pair202)<=10:#print out the result in some formate
    for i in pair202:
        print('  {0} {1}'.format(i[0],i[1]))
else:
    print('  {0} {1}'.format(pair202[0][0],pair202[0][1]))
    print('  {0} {1}'.format(pair202[1][0],pair202[1][1]))
    print('  {0} {1}'.format(pair202[2][0],pair202[2][1]))
    print('  {0} {1}'.format(pair202[3][0],pair202[3][1]))
    print('  {0} {1}'.format(pair202[4][0],pair202[4][1]))
    print('  ...')
    print('  {0} {1}'.format(pair202[-5][0],pair202[-5][1]))
    print('  {0} {1}'.format(pair202[-4][0],pair202[-4][1]))
    print('  {0} {1}'.format(pair202[-3][0],pair202[-3][1]))
    print('  {0} {1}'.format(pair202[-2][0],pair202[-2][1]))
    print('  {0} {1}'.format(pair202[-1][0],pair202[-1][1]))
print('5. Ratio of distinct word pairs to total: {0:.3f}'.format(len(pair202)/len(pair201)))
print()
print('Summary comparison')
if average_x>average_y:#compare the average len of two file and print the result out 
    print('1. {0} on average uses longer words than {1}'.format(file1,file2))
if average_x<average_y:
    print('1. {0} on average uses longer words than {1}'.format(file2,file1))
totalset=a|b
intersection=a&b #find the union and intersection then find the similarity
print('2. Overall word use similarity: {0:.3f}'.format(len(intersection)/len(totalset)))
print('3. Word use similarity by length:')
#it is part of the prase line and store the value in string then print out in some formate
dictionx=dict()
for m in x:
    
    length=str(len(m))
    
    if length in dictionx:
        dictionx[length].add(str((m)))
    else:
        dictionx[length]=set()
        dictionx[length].add(str((m)))
dictiony=dict()
for m in y:
    
    length=str(len(m))
    
    if length in dictiony:
        dictiony[length].add(str((m)))
    else:
        dictiony[length]=set()
        dictiony[length].add(str((m)))        
        



init=0
for v in list(dictionx.keys()):
    if int(v)>int(init):
        init=int(v)
    for h in list(dictiony.keys()):
        if int(h)>int(init):
            init=int(h)
        
for i in range(1,init+1):
    similar=0
    if str(i) in list(dictionx.keys()) and str(i) in list(dictiony.keys()):
        similarity = len(dictionx[str(i)] & dictiony[str(i)]) / len(dictionx[str(i)] | dictiony[str(i)])
        if i < 10:
            print('   {}: {:.4f}'.format(str(i), similarity))
        elif i>=10:
            print('  {}: {:.4f}'.format(str(i),similarity))
            
    elif i>=10:
        print('  {}: {:.4f}'.format(str(i),0))
    elif i<10:
        print('   {}: {:.4f}'.format(str(i),0))
    
        
#this one is store the discition pair into the set whcih remove the repeat one. then use the len of union and len of intersection to find the Word pair similarity
unit102=set()
for i in pair102:
    unit102.add(str(i))


unit202=set()
for j in pair202:
    unit202.add(str(j))

unitset=len(unit102|unit202)
interset=len(unit102&unit202)
    

pnum=interset/unitset
print('4. Word pair similarity: {0:.4f}'.format(pnum))


  




