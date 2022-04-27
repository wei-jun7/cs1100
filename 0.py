from hw5_util import get_grid
from hw5_util import get_start_locations



"""
This function is use to find the adjcent unit of tuple and -1 is make sure the number is bigger than 0. ALso, teh -2 is make sure the number 
in the range.
"""
def get_nbrs(tuple1):
    neighborlistpoint = []

    if tuple1[0] > 0  and tuple1[1] >-1:     
        neighborlistpoint.append((tuple1[0]-1 ,tuple1[1]))
        
    if tuple1[0] > -1 and tuple1[1] > 0: 
        neighborlistpoint.append((tuple1[0] , tuple1[1]-1))
        
    if tuple1[0] > -1 and tuple1[1] < len(get_grid(grid_number)[0])-2: 
        neighborlistpoint.append((tuple1[0] , tuple1[1]+1))
   
    if tuple1[0] < len(get_grid(grid_number))-2 and tuple1[1] > -1: 
        neighborlistpoint.append((tuple1[0]+1 , tuple1[1]))
        
    return neighborlistpoint
        
"""
This function is use to define the for loop and 2 if fucntion to find the size of the point with the largest increase in the adjacent tuple, and the location information of the point. At the end
we return the max1 and max1value.
"""

def max_nbr(tuple2):
    max1=""
    max1value= 0
    whethermax = 0
    for i in range(len(get_nbrs(tuple2))):
        if get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] > max1value and 0 < get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] - get_grid(grid_number)[tuple2[0]] [tuple2[1]] <= steph:
            max1value = get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]]
            max1= (get_nbrs(tuple2)[i][0] , get_nbrs(tuple2)[i][1])
        if get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] > max1value and get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] - get_grid(grid_number)[tuple2[0]] [tuple2[1]] > steph:
            whethermax = -1
    if max1=="" and max1value == 0 and whethermax ==-1:
        return (-1,-1)
    if max1=="" and max1value == 0 and whethermax !=-1:
        return (-1,0)
    return (max1,max1value)
"""
This fuction is do the similar job as max function but change for find the biggest one to the smallest one.At the end return the value 
for further calculation.
"""


def min_nbr(tuple2):
    min1=""
    min1value= 1000000000
    whethermax = 0
    for i in range(len(get_nbrs(tuple2))):
        if get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] < min1value and 0 < get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] - get_grid(grid_number)[tuple2[0]] [tuple2[1]] <= steph:
            min1value = get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]]
            min1= (get_nbrs(tuple2)[i][0] , get_nbrs(tuple2)[i][1])
        if get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] < min1value and get_grid(grid_number)[get_nbrs(tuple2)[i][0]] [get_nbrs(tuple2)[i][1]] - get_grid(grid_number)[tuple2[0]] [tuple2[1]] > steph:
            whethermax = -1
    if min1=="" and min1value == 1000000000 and whethermax ==-1:
        return (-1,-1)
    if min1=="" and min1value == 1000000000 and whethermax !=-1:
        return (-1,0)
    return (min1,min1value)


    
#########################################################################
"""
This part is ask for the user input the value for calcualtion
"""
grid_number= int (input ("Enter a grid index less than or equal to 3 (0 to end): "))
print(grid_number)

steph = int (input( "Enter the maximum step height: "))
print(steph)
choice1= str (input("Should the path grid be printed (Y or N): "))
print(choice1)

#########################################################################
"""
This section print out how big of this matrix and it is similar to the previous work
"""
choice1= choice1.lower()
print("Grid has",len(get_grid(grid_number)),"rows and",len(get_grid(grid_number)[0]),"columns")
#########################################################################
"""
This part is use the function we define before to calculation the global max which find the highest point and print out the value at the end
"""


maxivalue=0
maxi = ""
for i in range(len(get_grid(grid_number))):
    for j in range(len(get_grid(grid_number)[0])):
        if int(get_grid(grid_number)[i][j]) > maxivalue:
            maxivalue = get_grid(grid_number)[i][j]
            maxi=(i,j)
print("global max:",maxi,maxivalue)

#########################################################################
"""
In here we use the for loop function to find two different paths to startPoint and append the value which the loction of each move in the list which call total
Then we will compare the result to find the Path Grid at the end. Also, We should make sure the order of this for loop or in if statement
because the problem is which condition should be at frist and if it not do well will let the function end in the wrong place 

"""

startpoint = get_start_locations(grid_number)
total =[]
for i in range(len(startpoint)):
    print("===")
    
    print("steepest path")
    steepest=str(startpoint[i])+ " "
    location = startpoint[i]
    boxlenth1= 0
    total.append(location)
    while max_nbr(location)[0] != -1:
        if boxlenth1 == 4:
            steepest += "\n"
            boxlenth1-=5
        
        location = max_nbr(location)[0]
        total.append(location)
        steepest = steepest + str(location) + " "
        boxlenth1 +=1
    
    print(steepest)
    if max_nbr(location)[1]==-1:
        print("no maximum")
    if location == maxi:
        print("global maximum")
    elif location != maxi and max_nbr(location)[1]!=-1:
        print ("local maximum")
    print("...")
    
    
    
      
    boxlenth2= 0
    print("most gradual path")
    gradual=str(startpoint[i]) + " "
    location = startpoint[i]
    boxlenth= 0
    total.append(location)
    while min_nbr(location)[0] != -1:
        if boxlenth2 == 4:
            gradual += "\n"
            boxlenth2 -=5
        
        location = min_nbr(location)[0]
        total.append(location)
        
        gradual = gradual + str(location) + " "
        boxlenth2 +=1
    
    print(gradual)
    if min_nbr(location)[1]==-1:
        print("no maximum")
    if location == maxi:
        print("global maximum")
    elif location != maxi and min_nbr(location)[1]!=-1:
        print ("local maximum")
#########################################################################
"""
At the end, we use the data for the list call total to calculate different results base on the frequency of different positions
Next, we will use the for loop to put the result into the matrix and print it out at the end of the task.
"""
print ("===")
pathgrid = ""
for x in range(len(get_grid(grid_number))):
    pathgrid += '\n'
    for y in range(len(get_grid(grid_number)[0])):
       
        pathgrid += "  "
        pathgrid += str(total.count((x,y)))
    
pathgrid=pathgrid.replace("0",".")
if choice1 == "y":    
    print ("Path grid{}".format(pathgrid))
