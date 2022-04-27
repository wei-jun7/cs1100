def ranking_order(L2):
    L1=L2.copy()
    time=0
    for k in range(len(L1)-1):
        if L1[k]< L1[-1]:
            time+=1
    L1.pop()
    if L1==[]:
        return 0
    else:
        return time + ranking_order(L1)
        
Customers={'Customer_3':[4,3,5,2,1],'Customer_5': [1,3,4,2,5],'Customer_1':[5,4,3,2,1],\
           'Customer_4':[4,5,2,1,3],'Customer_2':[2,3,4,1,5],'Customer_10':[3,1,2,4,5],\
           'Customer_11':[2,5,1,4,3],'Customer_16':[1,2,4,5,3],'Customer_22':[5,1,3,4,2],\
           'Customer_100':[3,2,1,4,5]}


    
def nearest_user(u1,Customer):
    u1DM= ranking_order(Customer[u1])
    Customers=Customer.copy()
    Customers.pop(u1)
    DMs=[]
    fiveranks=list(Customers.values())
    indexs=[]
    
    for index in range(len(fiveranks)):
        indexs.append(ranking_order(fiveranks[index]))
    
    
    Customername = list(Customers.keys())
    for k in range(len(indexs)):
        j=[]
        
        j.append(ranking_order(fiveranks[k]))
        j.append(Customername[k])
        DMs.append(j)
    
    [['Customer_3',2],['Customer_3',8],['Customer_3',3],\
     ['Customer_3',3],['Customer_3',7],['Customer_3',8],\
     ['Customer_3',5],['Customer_3',8],['Customer_3',4],\
     ['Customer_3',7]]
    DMs.sort(reverse=True)
    
    difference = 100
    for index in indexs:
        if abs( index - u1DM)< difference :
            difference =abs(index-u1DM)
            
    similarlist=[]
    for k in DMs:
        if k.count(u1DM + difference) != 0 or k.count(u1DM - difference) != 0 :
            similarlist.append(k[1])
    
    similarlist.sort()
    return similarlist

if __name__ =="__main__":

    name =str( input('Please enter the customer name =>')).strip()
    print(name)
    
    if name in Customers:
        print('The dissimilarity metric for this customer is', ranking_order(Customers[name]))
        print('----------------------------------------\nSimilar User(s) And Recommendations:\n----------------------------------------')
        matelist=list(nearest_user(name, Customers))
        for mate in matelist:
            print(mate)
            if Customers[mate].index(5) == Customers[name].index(5):
                print('No recommendations for this user now')
            else:
                print('Customers who chose movie number {} also chose movie number {}'.format(Customers[name].index(5)+1,Customers[mate].index(5)+1))
    if name not in Customers:
        print('Please enter a valid customer name')
        
    
        
