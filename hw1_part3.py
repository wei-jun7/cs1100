# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:14:24 2021

@author: LiWeiJun
"""

character= input("Enter frame character ==> ")
print(character)

height= int(input("Height of box ==> "))
print(height)

wide= int(input("Width of box ==> "))
print(wide)
print()


a=" "*int(((wide-2-(len(str(wide)+str(height))+1))//2))
s=" "*int((wide-2-(len(str(wide)+str(height))+1))//2 +((wide-2-(len(str(wide)+str(height))+1))%2))
d=(height-3)//2
f=(height-3)//2 + (height-3)%2

middlepart="\n" + character + " "*(wide-2) + character

print("Box:")    
            
print(character*wide,end="")
print(middlepart*d)
print(character,a,wide,"x",height,s,character,sep="",end="")
print(middlepart*f)
print(character*wide)