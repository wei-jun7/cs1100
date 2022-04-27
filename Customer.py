class garden(object):
    def __init__(self,x= -1 ,y= -1,z= {-1} ):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        name= self.x.capitalize()
        area=round(self.y,1)
        average=round(self.z,1)
        return "{} require a sq.ft area of {}\nAnd average plant height  is {}".format(name,area,average)
    def water_required(self):
        amount= 0.5* self.y + 0.3* self.z
        return amount
