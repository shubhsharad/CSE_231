import math

class Vector(object):
   
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
       
    def __str__(self):
        return '{:.2f}, {:.2f}'.format(self.__x, self.__y)
   
    def __repr__(self):
        return self.__str__()
   
    def __add__(self, vector):
       
        x1=vector.__x+self.__x
        y1=vector.__y+self.__y
       
        return Vector(x1,y1)
           
    def __sub__(self, vector):
        x1=vector.__x-self.__x
        y1=vector.__y-self.__y
       
        return Vector(x1,y1)
   
    def __mul__(self, inp):
        if type(inp)==Vector:
            x1=inp.__x*self.__x
            y1=inp.__y*self.__y
            return x1+y1
        else:
            return Vector(inp*self.__x,inp*self.__y)
           
   
    def __rmul__(self, n):      
        return self.__mul__(n)
   
    def __eq__(self, vector):
        x1 = self.__x == vector.__x
        x2 = self.__y == vector.__y
       
        return x1 and x2
   
    def magnitude(self):
        magnitude = math.hypot(self.__x, self.__y)
        return magnitude
   
    def unit(self):
        try:
            m = self.magnitude()
           
            self.__x/=m
           
            self.__y/=m
           
        except ValueError:
            print('Cannot convert zero vector to a unit vector')
           
    # def main():
    #     string = __str__()
       
a1=Vector(1,2)
a2=Vector(3,4)
print(a1+a2)

b1=Vector(56,12)
b2=Vector(13,42)
print(b2-b1)

c1=Vector(26,5)
c2=Vector(23,12)
print(c1*c2)
print(2*c1)

print(c1.magnitude())
c1.unit()
print(c1)
        
        
        