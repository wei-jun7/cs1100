# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 00:19:45 2021

@author: LiWeiJun
"""



#import the moduel we need
import math
# this function is use to find the how many tourist are there base on the number of bear
def numtor(numbear):
    
    if numbear<4 or numbear>15:
        tourists=0
    elif 4<=numbear<=10:
        tourists=numbear*10000
    elif 10<numbear:
        tourists=100000+20000*(numbear-10)
    return tourists
# use max function to let number of bear and number of berry no be negative and use the len function to find the space of sheet in different value of result. the last step is renew the value at the end
def find_next(numbear,numberry,tourists):
    for x in range(2,11):
        tour = numtor(numbear)
        bears_next = max(math.floor(numberry /(50*(numbear+1)) + numbear*0.60 - (math.log(1+tour,10)*0.1)),0)
        berries_next = max((numberry *1.5) - (numbear+1)*(numberry /14) - (math.log(1+tour,10)*0.05), 0)
        tour = numtor(bears_next)
        space = " "*(10- len(str(x)))
        space2 = " "*(10- len(str(bears_next)))
        space3 = " "*(8- len(str(int(berries_next))))
        space4 = " "*(10-len(str(numtor(bears_next))))
        print("{0}{1}{2}{3}{4:.1f}{5}{6}{7}".format(x, space, bears_next,space2,berries_next, space3, tour, space4))
        bear1.append(bears_next)
        berry1.append(berries_next)
        t1.append(tour)
        numberry = berries_next
        numbear = bears_next

   

if __name__ == "__main__":    
#ask user to input the value
    numbear=int(input('Number of bears => '))
    print(numbear)
    
    numberry=input('Size of berry area => ')
    print(numberry)
    numberry= float(numberry)
    
    #print out the initial line of our sheet
    print('Year      Bears     Berry     Tourists  ')
    
    print('1        ', numbear," "*(8- len(str(numbear))) ,numberry," "*(8- len(str(numberry))) ,numtor(numbear), " "*(9-len(str(numtor(numbear)))))
    #give the variale in different value and use sort function to rearrange it to find the min and max
    tour = 0
    
    bear1 = [numbear]
    berry1 = [numberry]
    t1 = [numtor(numbear)]
    find_next(numbear, numberry, tour)
    bear1.sort()
    berry1.sort()
    t1.sort()
    
    #this is the function to print the Min and max
    print('\nMin:     ',bear1[0],' '*(8-len(str(min(bear1)))),'{:.1f}'.format (berry1[0])," "*(6- len(str(int(berry1[0])))),t1[0],' '*(8-len(str(min(t1)))),
          '\nMax:     ',bear1[-1]," "*(8-len(str(max((bear1))))) ,'{:.1f}'.format(berry1[-1]),' '*(6- len(str(int(berry1[-1])))),t1[-1],' '*(9-len(str(max(t1)))))
    
    
    
    
    
    
    
    
    
