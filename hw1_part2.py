# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 23:56:43 2021

@author: LiWeiJun
"""
import math as m

Min=input(('Minutes ==> '))
Min=int(Min)
print(Min)
Sec=input(('Seconds ==> '))
print(Sec)
Sec=int(Sec)
Miles=input(('Miles ==> '))
print(Miles)
Miles=float(Miles)

Target=input(('Target Miles ==> '))
print(Target)
Target=float(Target)

print()
pace_min=int((Min*60+Sec)/Miles//60)
pace_sec=int((Min*60+Sec)/Miles%60)
print("Pace is",pace_min,'minutes and',pace_sec,'seconds per mile.')
speed=(Miles/((Sec/60+Min)/60))
print("Speed is {:.2f}".format(speed),"miles per hour.")
run_min=((Target/speed)*60)
run_sec=(((Target/speed)*60*60%60))
print("Time to run the target distance of {:.2f}".format(Target),"miles is {:.0f}".format(m.floor(run_min)),"minutes and {:.0f}".format(m.floor(run_sec)),"seconds.")