# -*- coding: utf-8 -*-
"""
This function to evaltion the json and base on condition it  the user give
"""
#import the moduel to evaltion the json file
import json
'''
#This function determinate the x in the name of Twitter and the len of rate bigger than 3
#if not fit the condition it will return -1 and the function will stop in the another for loop function
'''
def average_twitter_rating(x):
    if x in ratecode and len(ratings[str(x)])>=3:
        return sum(ratings[str(x)])/len(ratings[str(x)])
    else:
        return -1
        

if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    #read the json file
    
    #use list to store the key value 
    moviecode=list(movies.keys())
    ratecode=list(ratings.keys())
    
    minyear=int(input('Min year => '))  #ask user to input value
    print(minyear)

    
    maxyear=int(input('Max year => '))        #ask user to input value  
    print(maxyear)

    
    w1=input('Weight for IMDB => ').strip()    #ask user to input value
    print(w1)
    w1=float(w1)
    
    w2=input('Weight for Twitter => ').strip()  #ask user to input value
    print(w2)
    w2=float(w2)
    
    ty=input('\nWhat genre do you want to see? ').strip()          #ask user to input value
    print(ty)
    ty=ty.title()#change the format
    '''
    use the list to store data and use if condition to find out the total rate between min and max year
    then append to the list with the code value and the genre in the movie
    '''
    
    allmovie=list()
    for i in moviecode:
        if minyear<= movies[str(i)]['movie_year'] <= maxyear:

            if average_twitter_rating(str(i))>0:
                totalrate=(w1 * movies[str(i)]['rating'] + w2 * average_twitter_rating(str(i))) / (w1 + w2)
                
                allmovie.append((totalrate,i,movies[i]['genre']))
    '''
    sort list allmovie list and use while function to to ask use input the genre and base on
    condition of genre input.
    '''
                
    allmovie=sorted(allmovie)            
    while ty.lower() != 'stop':
        
        storelist=[]
        for i in allmovie :
            if ty in i[2]:
                storelist.append(i) #use for loop to apppend the code for the move base on the genre
        if len(storelist)==0:                    
            print('\nNo {0} movie found in {1} through {2}'.format(ty,minyear,maxyear))   #print out the result and base on the condition
        else:                               
            print('\nBest:')                
            print('        Released in {0}, {1} has a rating of {2:.2f}'.format(movies[storelist[-1][1]]['movie_year'],movies[storelist[-1][1]]['name'],storelist[-1][0]))
            print('\nWorst:')                
            print('        Released in {0}, {1} has a rating of {2:.2f}'.format(movies[storelist[0][1]]['movie_year'],movies[storelist[0][1]]['name'],storelist[0][0]))
                                             
        ty=input('\nWhat genre do you want to see? ').strip()       
        print(ty)
        ty=ty.title()
        '''
        ask user to input again and see it meet the condition or not
        '''
            
            