# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:57:02 2021

@author: LiWeiJun
"""

import json
if __name__ == "__main__":                          ##copy the given file
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

allmovie=list(movies.keys())            ##make a list for all movie code in imdb
twrate=list(ratings.keys())            ##make a list for all movie code in twitter

minyear=input('Min year => ')           ##input the minimum year
print(minyear)
minyear=int(minyear)

maxyear=input('Max year => ')           ##input the maximum year
print(maxyear)
maxyear=int(maxyear)

wimdb=input('Weight for IMDB => ')      ##input the rate for imdb score
print(wimdb)
wimdb=float(wimdb)

wtw=input('Weight for Twitter => ')      ##input the rate for twitter score
print(wtw)
wtw=float(wtw)

movierate=[]                            ##create a list for all movies in the given year range,movie code, scores using rate and movie type in this
for i in allmovie:
    if minyear<=movies[i]['movie_year']<=maxyear :             ##make sure this movie in the range 
        if twrate.count(i)!=0 and len(ratings[i])>=3:
                    rate=(movies[i]['rating']*wimdb+(sum(ratings[i])/len(ratings[i]))*wtw)/(wimdb+wtw)
                    movierate.append((rate,i,movies[i]['genre']))               

m=sorted(movierate)                 ##using sorted to sort these movies according to new rate

k=0
while k<1:
    ty=input('\nWhat genre do you want to see? ')         ##let user input the type of movie he/she wants to watch
    print(ty)
    if ty=='sci-fi':                        ##since capitalied 'sci-fi' will be 'Sci-fi', which is different from what we want 'Sci-Fi', transfer this in special way                                          ##using if to make sure it transfers into right string
        ty='Sci-Fi'
    else:
        ty=ty.capitalize()                  ##other words can just use capitalize to transfer    
    okl=[]                                  ##record all movies that is in this type
    if ty!='Stop':                          ##if not type in stop, keep running
        for i in m:                         ##using all of list in movie in year range as input
            if i[2].count(ty)!=0:           ##if there is a tag is same to the type
                okl.append(i)               ##add this list into the user wants to see list
        if len(okl)==0:                     ##the possibility that no film is in this type
            print('\nNo {0} movie found in {1} through {2}'.format(ty,minyear,maxyear))
        else:                               ##ouput the best and worst
            print('\nBest:')                ##since the list of list of movies in range year is sorted before, it doesnot need to sorted again and last one is best
            print('        Released in {0}, {1} has a rating of {2:.2f}'.format(movies[okl[-1][1]]['movie_year'],movies[okl[-1][1]]['name'],okl[-1][0]))
            print('\nWorst:')                ##since the list of list of movies in range year is sorted before, it doesnot need to sorted again and first one is worst
            print('        Released in {0}, {1} has a rating of {2:.2f}'.format(movies[okl[0][1]]['movie_year'],movies[okl[0][1]]['name'],okl[0][0]))
    else:                                   ##if type in stop, stop this loop
        break