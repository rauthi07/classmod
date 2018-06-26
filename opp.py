#Q1
'''class Animal:
    gender=' '
    def __init__(self,name,place,sound):
         self.name=name
         self.place=place
         self.sound=sound
    def name(self):
        return self.name()
    def place(self):
        return self.place()
    def sound(self):
        return self.sound()
    def display(self):
        print('name:{},place:{},sound:{}'.format(self.name, self.place, self.sound), end=' ')
class Tiger(Animal):
    gender='male'
T1=Tiger('tiger','gujrat','roar')
T1.display()'''

#Q2 output
'''A B
A B'''


#Q4
'''class Shape:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
    def getarea(self, area):
        self.area = area
class Rectangle(Shape):
        def __init__(self, breadth, length):
            self.breadth = breadth
            self.length = length
        def rectangle_area(self):
            return self.length * self.breadth
class Square(Shape):
        def __init__(self, length):
            self.length = length
        def Square_area(self):
            return self.length ** 2
R1=Rectangle(10,20)
print(R1.area())'''









