# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:48:32 2021

@author: LiWeiJun
"""
#import the moduel we need for the calculation
from hw5_util import num_grids as ng
from hw5_util import get_grid as gg
from hw5_util import get_start_locations as gl
from hw5_util import get_path as gp

#This function is use get the neighbor tuple of tuple we put in and return list of tuple
def get_nbrs(x):
    nbrslist=[]
    if x[0]>0 and x[1]>-1:
        nbrslist.append((x[0]-1,x[1]))
        
    if x[0]>-1 and x[1]>0:
        nbrslist.append((x[0],x[1]-1))
    
    if x[0]>-1 and x[1]<len(gg(grid_number)[0])-2:
        nbrslist.append((x[0],x[1]+1))
        
    if x[0]<len(gg(grid_number))-2 and x[1]>-1:
        nbrslist.append((x[0]+1,x[1]))
        
    
    return nbrslist





#main program
if __name__== '__main__':
    total=ng
    grid_number=int(input('Enter a grid index less than or equal to 3 (0 to end): '))#ask user to input the value
    print(grid_number)
    grid=str(input('Should the grid be printed (Y or N): '))#ask user to input the value
    print(grid)
    grid=grid.lower()#low case can match the condition we give
    gridbox=''
    i=-1
    j=0#initial
    if grid=='y':
        while i< len(gg(grid_number))-1:#use while function to get the string of grid and print it out at the end
            gridbox+='\n'
            i+=1
            j=0
            while j<len(gg(grid_number)[0]) and i< len(gg(grid_number)):
                gridbox += " "*(4-len(str(gg(grid_number)[i][j])))
                gridbox += str(gg(grid_number)[i][j])
                j+=1
                
                
        
        print("Grid {}{}".format(grid_number,gridbox))
        
    print("Grid has {} rows and {} columns".format(len(gg(grid_number)),len(gg(grid_number)[0])))#print out the value we need 
    #use for loop to get all the neighbor value and print it out
    startpoint=gl(grid_number)
    for o in range(len(startpoint)):  
        Neighbors = get_nbrs(startpoint[o])
        neighborlist = ""
        for k in range(len(Neighbors)):
            neighborlist += " "
            neighborlist += str(Neighbors[k])
        print("Neighbors of {}:{}".format(startpoint[o],neighborlist))
          
    upward= 0
    downward= 0    
    change = 0   
    u=-1#initial
  #use whlie loop to compare the data from the get_path(gp) and print out the value we want and the order of if function is important.
    while u<len( gp(grid_number))-1:
        if get_nbrs(gp(grid_number)[u]).count(gp(grid_number)[u+1]) == 1:
            
            next_value = gg(grid_number) [ gp(grid_number)[u+1][0] ] [ gp(grid_number)[u+1][1] ] 
            current_value = gg(grid_number) [ gp(grid_number)[u]  [0] ] [ gp(grid_number)[u]  [1] ] 
            
            change = next_value-current_value
            if change < 0 :
                downward -= change
            elif change > 0:
                upward += change
        
        u+=1
        if u==len(gp(grid_number))-1:
            print("Valid path")
            print("Downward {}".format(downward))
            print("Upward {}".format(upward))
            
        elif get_nbrs(gp(grid_number)[u]).count(gp(grid_number)[u+1]) == 0:
            print("Path: invalid step from {} to {}".format ( gp(grid_number)[u] , gp(grid_number)[u+1] )  )
            break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    