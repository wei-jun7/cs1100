# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:13:41 2021

@author: LiWeiJun
"""
import math as m
#import the model we need
def find_volume_sphere(radius):
    return radius**3*4/3*m.pi
def find_volume_cube(side):
    return side**3
#define the function of volume



if __name__ == "__main__":
    radius=input("Enter the gum ball radius (in.) => ")
    print(radius)
    radius=float(radius)
    weekly_sale=int(input("Enter the weekly sales => "))
    print(weekly_sale)
    print()
    
    #ask the user input the value
    total_gum_ball=m.ceil(1.25*weekly_sale)
    #Find the target sale which how many the gum ball in totall
    side=m.ceil((total_gum_ball**(1/3)))
    #Find the how many side lenght of gum ball on each side
    edgelength=side*radius*2
    #Find the side of machine
    
    
    
    #print out the result and be award the format is {:.2f}
    print("The machine needs to hold" ,side, "gum balls along each edge.")
    print("Total edge length is {:.2f} inches.".format(edgelength))
    print("Target sales were ",str(total_gum_ball)+", but the machine will hold",side**3-total_gum_ball, "extra gum balls.")
    print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(find_volume_cube(edgelength)-find_volume_sphere(radius)*total_gum_ball))
    print("or {:.2f} cubic inches if you fill up the machine.".format(find_volume_cube(edgelength)-find_volume_sphere(radius)*side**3))
    
    
    
    