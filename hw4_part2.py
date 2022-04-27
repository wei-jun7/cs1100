# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 02:18:25 2021

@author: LiWeiJun
"""
#import the moduel we need for the function
from hw4_util import part2_get_week as wk
from hw4_util import print_abbreviations as ab

#This Function is use the wk funtion to find the list of data we want
#then use index of data to find the state data and calculate teh how many people 
#get infection
def daily(week,state1):
    stateindex=state.index(state1)
    status= wk(week)[stateindex]
    peopleposivetotal=0
    for i in range(2,9):
        peopleposivetotal+=status[i]
    peopleinfect = float(peopleposivetotal/7/status[1]*100_000)
    return peopleinfect

#This Function is use the wk funtion to find the list of data we want
#then use index of data to find the state data and calculate teh rate
def  pct(week, state1):
    stateindex=state.index(state1)
    status= wk(week)[stateindex]
    peopleposivetotal=0
    total=0
    for i in range(2,9):

        peopleposivetotal+=status[i]
    
    for j in range(2,16) :

        total+=status[j]
    rate=peopleposivetotal/total*100  
    
    return rate
#use the list to store the data and use while loop to go through each list
#and use different condition to append it or not. next call the ab function
def quar(week):
    Qstate=[]
    i=0
    while i<len(state):
        
        if daily(week,state[i]) >10 or pct(week,state[i])>10:
            Qstate.append(state[i])
    
        i+=1
    Qstate.sort()
    print("Quarantine states:")
    ab(Qstate)


#use the while function to go throught the list and replace the hightnumber and 
#return the statename at the end
def high(week):
    highnumber=0
    highstate=""
    i=0
    while i<len(state):
        if daily(week, state[i]) > highnumber:
            highstate= state[i]
            highnumber = daily(week, state[i])
        i+=1
    
    return [highstate,highnumber]
    
if __name__ == '__main__':    
        #this list show that the list of state and statelist conver it to be a string
        
        state = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', \
             'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', \
                 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', \
            'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', \
                'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
        statelist = " ".join(state)
        #use the x as initial to judge the while will be continous or not.
        x=True
        
        while x:
            print('...')  
            week = int(input("Please enter the index for a week: "))#ask user to input the data
            print(week)
            if week <0:#if less than the 0 week the program will be end
                x=False
            elif week > 34:#if more than the 34 week the program will be show the result
                print("No data for that week")
            elif week >=0 and week<35 :
                choice = str(input("Request (daily, pct, quar, high): ")).strip()#ask user to input the value 
                print(choice)
                choice= choice.lower()#change it for further calculation
                if choice == "daily":
                    STATE =str(input("Enter the state: ")).strip()
                    print(STATE)
                    STATE=STATE.upper()
                    if statelist.find(STATE)== -1:
                        print('State',STATE,'not found')
                    else:
                        print("Average daily positives per 100K population: {:.1f}".format(daily(week, STATE)))
                    
                if choice == "pct":
                    STATE =str(input("Enter the state: ")).strip()
                    print(STATE)
                    STATE= STATE.upper()
                    if statelist.find(STATE)==-1:
                        print('State',STATE,'not found')
                    else:            
                        print("Average daily positive percent: {:.1f}".format(pct(week,STATE)))
                    
                if choice == "quar":
                    quar(week)
                    
                if choice == "high":
                    high(week)
                    print("State with highest infection rate is {}".format(high(week)[0]))
                    print("Rate is {:.1f} per 100,000 people".format(high(week)[1]))
                if  choice != "high" and choice != "pct" and choice != "daily" and choice != "quar":
                    print("Unrecognized request")
        
        # use if function to judge condition and print out the result
        
