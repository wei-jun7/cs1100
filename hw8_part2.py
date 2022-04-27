
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 23:19:12 2021

@author: LiWeiJun
"""
import json

class Bear(object):
    def __init__(self,x0):
        
        self.data=x0
        
        
    def __str__(self):
        
        bear='Active Bears:'
        
        for i in self.data:
            a='('+str(i[0])+','+str(i[1])+')'
            bear=bear+'\n'+'Bear at {0} moving {1}'.format(a,i[2])
        
        return bear
    def move(self):
        berry_field=data["berry_field"]
        for i in self.data:
            if i[2]=="N" :
                 u=0
                 u+=berry_field[i[0]][i[1]]
        
                 berry_field[i[0]][i[1]]=0
                 while u<30:
                    i[0]-=1
                   
                    u+=berry_field[i[0]][i[1]]
                    berry_field[i[0]][i[1]]=0
                        
               
            if i[2]=='E':
                u=0
                u+=berry_field[i[0]][i[1]]
        
                berry_field[i[0]][i[1]]=0
                while u<30:
                     
                    i[1]+=1
                    if i[0]<0 and i[1]<0:
                        return print((i[0],i[1]))  
                    u+=berry_field[i[0]][i[1]+1]
                    berry_field[i[0]][i[1]]=0
                    
                    # if bear.row < 0 or bear.row > len(field.field)-1 or bear.col < 0 or bear.col > len(field.field)-1:
                    #     print("{} - Left the Field".format(bear))                    
                   
                        
            if i[2]=='W':
                u=0
                u+=berry_field[i[0]][i[1]]
        
                berry_field[i[0]][i[1]]=0
                while u<30:
                   i[1]-=1 
                   u+=berry_field[i[0]][i[1]-1]
                   berry_field[i[0]][i[1]]=0
                if i[0]<0 and i<[1]:
                    return print((i[0],i[1]))       
            if i[2]=='S':
                u=0
                u+=berry_field[i[0]][i[1]]
        
                berry_field[i[0]][i[1]]=0
                while u<30:
                    i[0]+=1
                    
                    u+=berry_field[i[0]+1][i[1]]
                    berry_field[i[0]][i[1]]=0
                        
            if i[2]=='NE':
                u=0
                u+=berry_field[i[0]][i[1]]
        
                berry_field[i[0]][i[1]]=0
                while u<30:

                    i[0]-=1
                    i[1]+=1
                    u+=berry_field[i[0]][i[1]]
                    berry_field[i[0]][i[1]]=0
                    
            if i[2]=='NW' :
                
                u=0
                
                u+=berry_field[i[0]][i[1]]
                berry_field[i[0]][i[1]]=0
                while u<30:
                    i[0]-=1
                    i[1]-=1
                    u+=berry_field[i[0]][i[1]]
                    berry_field[i[0]][i[1]]=0
                    if i[0]<0 and i[1]<0:
                        return print((i[0],i[1]))
            if i[2]=='SW':
                u=0
                u+=berry_field[i[0]][i[1]]
                berry_field[i[0]][i[1]]=0
                while u<30:
                    i[0]+=1
                    i[1]-=1
                    u+=berry_field[i[0]][i[1]]
                    berry_field[i[0]][i[1]]=0
            if i[2]=='SE':
                u=0
                u+=berry_field[i[0]][i[1]]
                berry_field[i[0]][i[1]]=0
                while u<30:
                    i[0]+=1
                    i[1]+=1
                    u+=berry_field[i[0]][i[1]]
                    berry_field[i[0]][i[1]]=0  
                    
                if i[0]<0 and i<[1]:
                    return (i[0],i[1])
    def counter(x):
        
        
        for ni in data["active_tourists"]:       
            for nk in data["active_bears"]:      
                if ni[0]==nk[0] and nk[1]==ni[1]:
                    list1=ni
                    data["active_tourists"].remove((ni))  
        return  list1         
        for i in range(1,5):
            if i %2==0:
                data["active_tourists"].append((list1)) 
        print(data["active_tourists"])
class BerryField(object):
    def __init__(self,z0):
        self.row=len(z0)
        self.col=len(z0[0])
        self.berry_field=z0
    def __str__(self):
        
        d={}
        
        b=0
        for i in self.berry_field:
            for j in i:
                if isinstance(j, int):
                    b+=j
        form='Field has {0} berries.'.format(b)
        
        for i,j in data["active_tourists"]:
            if isinstance(self.berry_field[i][j], int):
                d[(i,j)] = self.berry_field[i][j]
                self.berry_field[i][j] = 'T'
        for i,j,k in data["active_bears"]:
            if isinstance(self.berry_field[i][j], int):
             d[(i,j)] = self.berry_field[i][j]
             self.berry_field[i][j] ='B'
    
                     
        for ni in data["active_tourists"]:
            
            for nk in data["active_bears"]:
                
                if ni[0]==nk[0] and nk[1]==ni[1]:
                     
                   
                     self.berry_field[nk[0]][nk[1]]='X'  
                     
                    
        for number in data["berry_field"]:
            form=form+'\n'
            for j in number:
                form=form+str(j).rjust(4)
        print(d)
        for i , j in d:
              self.berry_field[i][j]=d[(i,j)]       
                    
        return form
    def grown(self):
        for i in range(0, len(self.berry_field)):
            for j in range(0, len(self.berry_field[0])):
                
                if isinstance(self.berry_field[i][j],int):
                    if 1<=self.berry_field [i][j]<10:
                        self.berry_field[i][j]+=1
                
        
    def spread(self):
        #self.berry_field[self.row-1][self.col-1]
        for i in range(len(self.berry_field)-1):
            for j in range(len(self.berry_field[0])-1):
                if not isinstance(self.berry_field[i][j],int) :
                    continue
                
                if  self.berry_field[i][j]==0 and (self.berry_field[i-1][j]==10 or  self.berry_field[i+1][j]==10 or self.berry_field[i][j+1]==10 or self.berry_field[i][j-1]==10): 
                    
                    self.berry_field[i][j]+=1
        l=self.col-1
        u=self.row-1            
        for k in range(len(self.berry_field[self.row-1])) :
            if self.berry_field[k][l]==0 and (self.berry_field[k-1][l]==10 or  self.berry_field[k+1][l]==10  or self.berry_field[k][l-1]==10): 
                
                self.berry_field[k][l]+=1
        for o in range(len(self.berry_field[self.col-1])) :
            if self.berry_field[u][o]==0 and (self.berry_field[u][o-1]==10 or  self.berry_field[u][o+1]==10  or self.berry_field[u-1][o]==10): 
                
                self.berry_field[u][o]+=1
                       
'''                            
def ok_to_add(row, col, num): 
    if not (row >= 0 and row <= 8 and col >= 0 and col <= 8 and num >= 1 and num <= 9):
        return False
    temp_bd =  data["berry_field"]
    temp_bd[row][col] = "X"
    for i in range(9):
        if isinstance(data["berry_field"][i],int):
            if int(temp_bd[row][i]) == 10:
                return False

    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if temp_bd[i][j].isdigit():
                if int(temp_bd[i][j]) == num:
                    return False
    return True                        
'''                    
class Tourist(object):
    def __init__(self,x0):
        self.data1=x0
        
        
    def __str__(self):
        tour="Active Tourists:"
        for i in self.data1:
            a='('+str(i[0])+','+str(i[1])+')'
            tour=tour+'\n'+'Tourist at {}, 0 turns without seeing a bear.'.format(a)

        return tour
        
if __name__=="__main__":
    #file=input('Enter the json file name for the simulation => ').strip()
    #print(file)
    #print()
    f = open("bears_and_berries_1.json")
    data = json.loads(f.read())
    
    berry=BerryField(data["berry_field"])

    bear=Bear(data["active_bears"])
    '''
    for bear in data["active_bears"]:
            bear[0]
            bear[1]
            bear[2]    
            '''
    print(berry)
    print()
    print(Bear(data["active_bears"]))
    print()
    print(Tourist(data["active_tourists"]))
    berry.grown()
    berry.spread()
    print(berry)
    print(bear.counter())
    bear.move()
    berry.grown()
    berry.spread()
    print(berry)
    
        
    
    
    #print(data["berry_field"])
    #print(data["active_bears"])
    #print(data["reserve_bears"])
    #print(data["active_tourists"])
    #print(data["reserve_tourists"])
    
    