#Q1
'''class Circle:
    def __init__(self,radius ):
        self.radius=radius
    def area(self):
        return self.radius**2*3.14
    def circumference(self):
        return self.radius*2*3.14
    def getarea(self,area):
        self.area=area
    def getcircumference(self,circumference):
        self.circumference=circumference
c1=Circle(1)
print(c1.area())
print(c1.circumference())'''

#Q2
'''class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def name(self):
         return self.name()
    def rollno(self):
        return self.rollno()
    def display(self):
        print('Name: {}, Rollno: {}'.format(self.name,self.rollno),end=' ')
s1=Student('amit',9)
s1.display()'''

#Q4
'''class MovieDetails:
    reviews='BAD'
    def __init__(self,Moviename, artistname,Yearofrelease , ratings ):
        self.Moviename=Moviename
        self.artistname=artistname
        self.Yearofrelease=Yearofrelease
        self.ratings=ratings
    def Moviename(self):
        return self.Moviename()
    def artistname(self):
        return self.artistname()
    def Yearofrelease(self):
        return self.Yearofrelease()
    def ratings(self):
        return self.ratings()
    def display(self):
        print(' Moviename:{},artistname:{},Yearofrelease:{},ratings:{}'.\
              format(self.Moviename,self.artistname,self.Yearofrelease ,self.ratings), end=' ')
        print('reviews:',self.reviews)
M=MovieDetails('abc','xyz',2018,7)
M.display()

M.reviews='GOOD'
M.display()'''

#Q5
'''class Expen:
    def __init__(self, expen, saving, total):
        self.expen = expen
        self.saving = saving
        self.total = expen + saving
    def display(self):
        print('expen: {}, saving: {},total{} '.format(self.expen, self.saving, self.total), end=' ')
s1 = Expen(100000, 135000, 'expen' + 'saving')
s1.display()'''