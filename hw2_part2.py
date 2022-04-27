# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 02:18:05 2021

@author: LiWeiJun
"""

import hw4_util

state = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
statelist = " ".join(state)


def daily(week,state1):
    stateindex = state.index(state1)
    status= hw4_util.part2_get_week(week)[stateindex]
    people = float((status[2]+status[3]+status[4]+status[5]+status[6]+status[7]+status[8])/7/status[1]*100000)
    return people

def pct(week,state1):
    stateindex = state.index(state1)
    status=  hw4_util.part2_get_week(week)[stateindex]
    percentage = (status[2]+status[3]+status[4]+status[5]+status[6]+status[7]+status[8])/(status[2]+status[3]+status[4]+status[5]+status[6]+status[7]+status[8]+status[9]+status[10]+status[11]+status[12]+status[13]+status[14]+status[15])*100
    average = round(percentage,1)
    return average

def quar(week):
    Qstate=[]
    i=0
    for i in range(len(state)):
        State = state[i]
        if daily(week,State) >10 or pct(week,State)>10:
            Qstate.append(State)
    Qstate.sort()
    print("Quarantine states:")
    hw4_util.print_abbreviations(Qstate)





def high(week):
    highnumber=0
    highstate=""
    for i in range(len(state)):
        if daily(week, state[i]) > highnumber:
            highstate= state[i]
            highnumber = daily(week, state[i])
    highcombine=[highstate,highnumber]  
    return highcombine
    



x=0

while x==0:
    print('...')  
    week = int(input("Please enter the index for a week: "))
    print(week)
    if week <0:
        x+=100
    elif week >=0 and week<35 :
        choice = str(input("Request (daily, pct, quar, high): "))
        print(choice)
        choice= choice.lower()
        if choice == "daily":
            STATE =str(input("Enter the state: "))
            print(STATE)
            STATE=STATE.upper()
            if statelist.find(STATE)==-1:
                print('State',STATE,'not found')
            else:
                print("Average daily positives per 100K population:",round(daily(week, STATE), 1))
            
        if choice == "pct":
            STATE =str(input("Enter the state: "))
            print(STATE)
            STATE= STATE.upper()
            if statelist.find(STATE)==-1:
                print('State',STATE,'not found')
            else:            
                print("Average daily positive percent: {}".format(pct(week,STATE)))
            
        if choice == "quar":
            quar(week)
            
        if choice == "high":
            print("State with highest infection rate is {}".format(high(week)[0]))
            print("Rate is {:.1f} per 100,000 people".format(high(week)[1]))
        if  choice != "high" and choice != "pct" and choice != "daily" and choice != "quar":
            print("Unrecognized request")
    elif week > 34:
        print("No data for that week")
    