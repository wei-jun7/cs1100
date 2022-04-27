# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:51:14 2021

@author: LiWeiJun
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:08:27 2020
In this part of the hw, there will be 4 inputs.
4 inputs that ask the user to put the min year, max year, Weight for IMDB, and the Weight for Twitter.
Then find all movies in movies made between min and max years (inclusive of both min and max years)
If a movie is not rated in Twitter, or if the Twitter rating has fewer than 3 entries, skip the movie.
Continue the loop that asking the movie name, stop the loop when the user ask to stop.
@author: Sijian Tao
"""


import json
def getMovie(minyear,maxyear,genre):
    '''
    This def is helping me to find the movieid in the file.And read it. 
    Because not all movies in movies.json have a rating in ratings.json, and not all movies in ratings.json have relevant info in movies.json.
    So there need some if judgments. 
    '''
    movieid=[]
    for i in movies.keys():
        temp=[]
        for j in movies[i]["genre"]:
            temp.append(j.lower())
        # print (temp)
        if movies[i]['movie_year']>=minyear and  movies[i]["movie_year"]<=maxyear and genre in temp and i in ratings.keys() and len(ratings[i])>=3:
            movieid.append(i)
    return movieid
def getScore(movielist,weight1,weight2):
    '''
    This def helps me to find the scores of the two movies. 
    If a movie is not rated in Twitter, or if the Twitter rating has fewer than 3 entries, skip the movie.
    
    '''
    score=[]
    for i in movielist:
        temp=0
        temp+=(movies[i]["rating"]*weight1)
        temp+=(sum(ratings[i])/len(ratings[i]))*weight2
        temp=temp/(weight1+weight2)
        score.append(temp)
    return score
        

#import json
if __name__ == "__main__":
    '''
    here is the main part of the code.
    '''
    movies = json.loads(open("movies.json").read()) 
    ratings = json.loads(open("ratings.json").read())
    
minyear=int(input("Min year => "))
print(minyear)
maxyear=int(input("Max year => "))
print(maxyear)
weight1=input("Weight for IMDB => ")
print(weight1)
weight1 = float(weight1)
weight2=input("Weight for Twitter => ")
print(weight2)
print()
weight2 = float(weight2)
while(True):
    genre=input("What genre do you want to see? ")
    print(genre)
    genre = genre.lower()
    if genre=="stop":
        break
    movieslist=getMovie(minyear,maxyear,genre)
    score=getScore(movieslist,weight1,weight2) 
    moviescore=[]
   
    for i in range(len(score)):
        moviescore.append(("{:.2f}".format(score[i]),movieslist[i]))
    moviescore=sorted(moviescore, reverse=True)
    if len(moviescore)>0:
        print()
        print("Best:")
        print("        Released in "+str(movies[moviescore[0][1]]["movie_year"])+", "+str(movies[moviescore[0][1]]["name"])+" has a rating of "+str(moviescore[0][0]))
        print()
        print("Worst:")
        print("        Released in "+str(movies[moviescore[-1][1]]["movie_year"])+", "+str(movies[moviescore[-1][1]]["name"])+" has a rating of "+str(moviescore[-1][0]))
        print()
    else:
        print()
        print("No "+genre.title()+" movie found in "+str(minyear)+" through "+str(maxyear))
        print()
   
    
    
# genre=input("What genre do you want to see? ")
    
'''    
minyear=2000
maxyear=2016
weight1=0.7
weight2=0.3
genre="Sci-Fi"
'''