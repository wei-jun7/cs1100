# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 23:19:12 2021

@author: LiWeiJun
"""
import json

class Bear(object):
    def __init__(self,x0=0,y0=0):
        self.x=x0
        self.y=y0
        
    def __str__(self):
        bear='Active Bears:'
        for i in data["active_bears"]:
            a='('+str(i[0])+','+str(i[1])+')'
            bear=bear+'\n'+'Bear at {0} moving {1}'.format(a,i[2])
        
        return bear
class BerryField(object):
    def __init__(self,x0=0,y0=0):
        self.x=x0
        self.y=y0
    def __str__(self):
        b=0
        for i in data["berry_field"]:
            for j in i:
                b+=j
        form='Field has {0} berries.'.format(b)
        for list1 in range(len(data["berry_field"])):
            for list2 in data["active_tourists"]:
                for list3 in data["active_bears"]:

 
                    if  list1==list2[0]:
                        data["berry_field"][list1][list2[1]]='T'
                    
                        
                   
                        
                    if list1==list3[0]:
                        data["berry_field"][list1][list3[1]]='B'   
                     
        for ni in data["active_tourists"]:
            
            for nk in data["active_bears"]:
                
                if ni[0]==nk[0] and nk[1]==ni[1]:
                    
                    data["berry_field"][nk[0]][nk[1]]='X'  
                    
                    
        for number in data["berry_field"]:
            form=form+'\n'
            for j in number:
                form=form+str(j).rjust(4)
       
                    
                    
                    
        return form
    

class Tourist(object):
    def __init__(self,x0=0,y0=0):
        self.x=x0
        self.y=y0
        
    def __str__(self):
        tour="Active Tourists:"
        for i in data["active_tourists"]:
            a='('+str(i[0])+','+str(i[1])+')'
            tour=tour+'\n'+'Tourist at {}, 0 turns without seeing a bear.'.format(a)

        return tour
    
    

        
if __name__=="__main__":
    file=input('Enter the json file name for the simulation => ').strip()
    print(file)
    print()
    f = open(file)
    data = json.loads(f.read())

    print(BerryField())
    print()
    print(Bear())
    print()
    print(Tourist())
    
    #print(data["berry_field"])
    #print(data["active_bears"])
    #print(data["reserve_bears"])
    #print(data["active_tourists"])
    #print(data["reserve_tourists"])
    
    