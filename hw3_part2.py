# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:56:08 2021

@author: LiWeiJun
"""
#this funtion is use the tell how the pokemon go 
def move_pokemon(row,column,direction, path):
    if direction=="n":
        new_row=row-path
        new_column=column   
        new_row=max(0,new_row)
    elif direction=="e":
        new_row=row
        new_column=column+path
        new_column=min(150,new_column)
    elif direction=="s":
        new_row=row+path
        new_column=column
        new_row=min(150,new_row)
    elif direction=="w":
        new_row=row
        new_column=column-path
        new_column=max(0,new_column)
    else:
        new_row=row
        new_column=column
        
    return new_row , new_column

#ask user to input the value we need
if __name__ == "__main__":
    turn = input('How many turns? => ')
    print(turn)
    turn = int(turn)
    pokemon_name = input('What is the name of your pikachu? => ')
    print(pokemon_name)
    pokemon_name=str(pokemon_name)
    frequency = input('How often do we see a Pokemon (turns)? => ')
    print(frequency)
    print()
    frequency = int(frequency)
    number_turn = 0
    print ('Starting simulation, turn' , number_turn, pokemon_name,'at (75, 75)')
    record = []
    """There have 3 value which i= how many turn t=when should be fight k = what turn now 
    use while to find repeat the ask the user input the value and at the end print out the 
    information we need base on the calculation
    
    """
    if turn==0:
        print(pokemon_name,'ends up at (75, 75), Record: []')
    else:
       row,column=75,75
       i=0
       t=0
       k=0
       while i<turn:
           direction = input('What direction does '+pokemon_name+' walk? => ')
           print(direction)
           direction = direction.lower()
       
           location = move_pokemon(row, column, direction, 5)
           row = location[0]
           column = location[1]
           i+=1
           t+=1
           k+=1
        
           if t < turn and t%frequency == 0:
               
                print('Turn', str(k)+',',pokemon_name,'at', location)
                encounter = input('What type of pokemon do you meet (W)ater, (G)round? => ')
                print(encounter)
                encounter = encounter.lower()
                if encounter == 'g':
                    location = move_pokemon(row, column, direction, -10)
                    print(pokemon_name, 'runs away to', location)
                    record.append('Lose')            
                elif encounter == 'w':
                   
                    location = move_pokemon(row, column, direction, 1)
                    print(pokemon_name,'wins and moves to', location)
                    record.append('Win')
                else:
                    record.append('No Pokemon')
                t=0
                row = location[0]
                column = location[1]
    
    
    
    
    
       print(pokemon_name,'ends up at '+str(location)+', Record:', record)
    
   
    
       

















