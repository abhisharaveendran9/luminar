class student:
    name:str
    age:int
    cls:str
    gender:str
    def set_student(self,name,age,cls,gender):
        self.name=name               #initializing instance variables
        self.age=age
        self.cls=cls
        self.gender=gender
    def print_student(self):
        print(self.name,self.age,self.cls,self.gender)

s1=student()           #object of student
s1.set_student("Abhi",25,"MCA","female")
s1.print_student()


class person:
    name:str
    age:int
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name,self.age)

p1=person(name="ram",age="25")
p1.print_person()


class bottle:
    material:str
    capacity:str
    price:int
    color:str
    def set_bottle(self,**kwargs):
        self.material=kwargs.get("material")
        self.capacity=kwargs.get("capacity")
        self.price=kwargs.get("price")
        self.color=kwargs.get("color")
    def open(self):
        print("open")
    def print_bottle(self):
        print(self.price,self.material,self.color,self.capacity)

bt=bottle()
bt.set_bottle(material="plastics",capacity="800ml",price=150,color="blue")  #++kwargs arguments
bt.print_bottle()



#course c,id,c_name,c_fee,c_year
class course:
    c_name:str
    c_id:str
    c_fee:int
    c_year:int
    def __init__(self,c_name,c_id,c_fee,c_year):
        self.c_name=c_name
        self.c_id=c_id
        self.c_fee=c_fee
        self.c_year=c_year
    def print_course(self):
        print(self.c_name,self.c_id,self.c_fee,self.c_year)

cr=course(c_name="BCA",c_id="B1001",c_fee=10000,c_year=2018)
cr.print_course()