# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:03:25 2021

@author: LiWeiJun
"""

#import the moduel we need for the calculation
from hw5_util import num_grids as ng
from hw5_util import get_grid as gg
from hw5_util import get_start_locations as gl

#This function is use get the neighbor tuple of tuple we put in and return list of tuple
def get_nbrs(x):
    nbrslist=[]
    if x[0]>-1 and x[1]<len(gg(grid_number)[0])-2:
        nbrslist.append((x[0],x[1]+1))
    if x[0]<len(gg(grid_number))-2 and x[1]>-1:
        nbrslist.append((x[0]+1,x[1]))    
       
    if x[0]>-1 and x[1]>0:
        nbrslist.append((x[0],x[1]-1))
    if x[0]>0 and x[1]>-1:
        nbrslist.append((x[0]-1,x[1]))

    
    
        
    
        
    
    return nbrslist
'''
we use this function to find the neighbor tuple have the max value which we can find the steeep path to the reach the globe/local  value
There use 3 parameter to calculation which max1 is use to get the location and max1value is use to get the value of it and another one is 
use to get no way to go 
'''
def max_nbrs(x):

    max1=""
    max1value= 0
    end = 0
    i=-1
    while i<len(get_nbrs(x)):
    
        if gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] > max1value and 0 <gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] - gg(grid_number)[x[0]] [x[1]] <= high:
            max1value = gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]]
            max1= (get_nbrs(x)[i][0] , get_nbrs(x)[i][1])

        if gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] > max1value and gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] - gg(grid_number)[x[0]] [x[1]] > high:
            end = -1
        i+=1      
    if max1=="" and max1value == 0 and end ==-1:
        return (-1,-1)
    if max1=="" and max1value == 0 and end!=-1:
        return (-1,0)
    return (max1,max1value)
    

'''
we use this function to find the neighbor tuple have the max value which we can find the gradual path to the reach the globe/local  value
There use 3 parameter to calculation which min1 is use to get the location and min1value is use to get the value of it and another one is 
use to get no way to go 
'''

def min_nbrs(x):
    min1value= 1000000000
    endpoint = 0
    min1=""
    i=-1
    while i <len(get_nbrs(x)):

        if gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] < min1value and 0 < gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] - gg(grid_number)[x[0]] [x[1]] <= high:
            min1value = gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]]
            min1= (get_nbrs(x)[i][0] , get_nbrs(x)[i][1])
        if gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] < min1value and gg(grid_number)[get_nbrs(x)[i][0]] [get_nbrs(x)[i][1]] - gg(grid_number)[x[0]] [x[1]] > high:
            endpoint = -1
        i+=1
    if min1=="" and min1value == 1000000000 and endpoint ==-1:
        return (-1,-1)
    if min1=="" and min1value == 1000000000 and endpoint !=-1:
        return (-1,0)
        
    return (min1,min1value)
    
    
''' this one is use to find the globe value or local value and return a list of location and value''' 

  
    
def max_value():
    maxvalue=0
    maxlist=[]
    for i in range(len(gg(grid_number))):
        for j in range(len(gg(grid_number)[0])):
            if int(gg(grid_number)[i][j])>maxvalue:
                maxvalue=gg(grid_number)[i][j]
                maxlist.append('('+str(i)+', '+str(j)+')')
    return (maxlist[-1],maxvalue)





if __name__== '__main__':
    total=ng
    grid_number=int(input('Enter a grid index less than or equal to 3 (0 to end): '))#ask user to input the value
    print(grid_number)
    high = int (input( "Enter the maximum step height: "))#ask user to input the value
    print(high)
    grid=str(input('Should the path grid be printed (Y or N): '))#ask user to input the value
    print(grid)
    grid=grid.lower()#low case can match the condition we give
    print("Grid has {} rows and {} columns".format(len(gg(grid_number)),len(gg(grid_number)[0])))#print out the value we need 
    max_value()
    print("global max: {} {}".format(max_value()[0],max_value()[1]))#print out the value base on  input the value
    
    startpoint = gl(grid_number)#ask user to input the value, and use this value to find the start point
    total =[]
    k=0
    '''
    In the start point we need to calculation the steep path and the gradual path which we nedd to print out the value of location for each start point
    '''
    while k<len(startpoint):
        print("===")
        print("steepest path")
        steepest=str(startpoint[k])+ " "
        location = startpoint[k]
        boxlenth1= 0
        total.append(location)
        x=0
        while max_nbrs(location)[0] != -1:
            location = max_nbrs(location)[0]
            total.append(location)
            boxlenth1 +=1#for this part we must get the information for steepest line and add count in the last time which it can avoid the extra space for it
            if boxlenth1 == 5 :
                steepest += "\n"
                boxlenth1-=5
            steepest = steepest + str(location) + " "
        
        
        print(steepest)
        
        if max_nbrs(location)[1]==-1:
            print("no maximum")
        if str(location) == max_value()[0]:
            print("global maximum")
        elif str(location) != max_value()[0] and max_nbrs(location)[1]!=-1:
            print ("local maximum")
        print("...")
        
        
    

        boxlenth2= 0
        print("most gradual path")
        gradual=str(startpoint[k]) + " "
        location = startpoint[k]
        total.append(location)
        x=0
        while min_nbrs(location)[0] != -1:
            location = min_nbrs(location)[0]
            total.append(location)
        
            boxlenth2 +=1
            if boxlenth2 == 5 :
                gradual += "\n"
                boxlenth2 -=5
            gradual = gradual + str(location) + " "
        
        
        print(gradual)

        if min_nbrs(location)[1]==-1:
            print("no maximum")
        if str(location) == max_value()[0]:
            print("global maximum")
        elif str(location) != max_value()[0] and min_nbrs(location)[1]!=-1:
            print ("local maximum")
            
        k+=1            
            
    '''       
    base on the condition the user give print out the result we want base on the data we collect.            
    '''        
            
    print ("===")
    print("Path grid")
    
    pathgrid = ""
    for x in range(len(gg(grid_number))):
        for y in range(len(gg(grid_number)[0])):
            pathgrid += "  "
            pathgrid += str(total.count((x,y)))
        pathgrid += '\n'
    pathgrid=pathgrid.replace("0",".")
    if grid == "y":    
        print (pathgrid,end='')
    























