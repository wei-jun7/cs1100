import Park
import json

filename = str(input("Enter the json file name for the simulation => ")).strip()
print(filename)
f = open(filename)
data = json.loads(f.read())


Clist = data["Customer"]
maximum = data["Station"]



for ele in range(len(Clist)):
    if Clist[ele][1] <Clist[ele][0]:
        Clist[ele][1] = 2*maximum-Clist[ele][1]





print(Park.Park(maximum , Clist),end="")
print('End of Iteration 1')

for cust in range(len(Clist)):
    if Clist[cust][0] ==1 and  Clist[cust][0] != Clist[cust][1]:
        Clist[cust][0]=''
    elif Clist[cust][1] ==1:
        Clist[cust][0]=Clist[cust][1]
        



for k in range(2, 2*maximum+1):
    P=0
    if k <=maximum:
        P =k
    if k > maximum and k <2*maximum:
        P =2*maximum-k
    if k== 2*maximum:
        P=1
    
    print("\n\n")
    
    form = '''------------------------------------------------------------
 Station                  Customer                   Tram   
------------------------------------------------------------
'''
    
    
    for line in range(maximum, 0, -1):
        indicatorL = ''        
        for position in range(len(Clist)):
            if Clist[position][0] == line:
                indicatorL += str(position+1)
                indicatorL += " "
        if len(indicatorL)%2 ==0:
            if line  ==P:
                form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(20-len(indicatorL)//2) + "   *T*    "
            if line != P:
                form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(20-len(indicatorL)//2)
        if len(indicatorL)%2 !=0:
            if line  ==P:
                form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(19-len(indicatorL)//2) + "   *T*    "
            if line != P:
                form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(19-len(indicatorL)//2)
            
        form += '\n' + '------------------------------------------------------------' + '\n'
    print(form,end="")
    print('End of Iteration {}'.format(k),end='')
    
    
    for cust in range(len(Clist)):
        if Clist[cust][0] ==P and  Clist[cust][0] != Clist[cust][1]:
            Clist[cust][0]=''
            
            
        if Clist[cust][1] ==P :
            Clist[cust][0]=Clist[cust][1]
        if Clist[cust][1] ==2*maximum-P and k > maximum:
            Clist[cust][0]=2*maximum- Clist[cust][1]
