class Tram(object):
    def __init__(self, final= -1 ):
        self.x = 1
        self.y = final
        self.z = 1
    def __str__(self):
        s = "The Tram is currently at station {} out of {}" .format(self.x , self.y )
        return s
    def move(self):
        if self.z <  self.y:
            self.x +=1
            
        if self.z == self.y:
            self.x-=1
            
        if self.z > self.y and self.z < (2* self.y) -1 :
            self.x -=1
            
        self.z +=1
        return self.x
t=Tram(3)
print(t)
t.move()
print(t)
