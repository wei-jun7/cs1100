class Park(object):
    
    
    
    def __init__(self, maximum=-1 , Clist=-1 ):
        self.x = maximum
        self.y = Clist
    
    def __str__ (self):
        form = '''------------------------------------------------------------
 Station                  Customer                   Tram   
------------------------------------------------------------
'''
    
    
        for line in range(self.x, 0, -1):
            indicatorL = ''        
            for position in range(len(self.y)):
                if self.y[position][0] == line:
                    indicatorL += str(position+1)
                    indicatorL += " "
            if len(indicatorL)%2 ==0:
                if line  ==1:
                    form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(20-len(indicatorL)//2) + "   *T*    "
                if line != 1:
                    form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(20-len(indicatorL)//2)
            if len(indicatorL)%2 !=0:
                if line  ==1:
                    form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(19-len(indicatorL)//2) + "   *T*    "
                if line != 1:
                    form =form + "    " + str(line) + " " * (26-len(str(line))-len(indicatorL)//2 ) + indicatorL + " "*(19-len(indicatorL)//2)
            
            form += '\n' + '------------------------------------------------------------' + '\n'
        return form

if __name__ =="__main__":
      
    print(Park(3,[[1,3],[3,1]]))