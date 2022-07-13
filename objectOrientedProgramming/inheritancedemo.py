#single inheritance
class parent:
    def phone(self):
        print("nokia")
    def bike(self):
        print("passion pro")

class child(parent):
    pass

ch=child()
ch.phone()
ch.bike()

#multilevel inheritances

class p1:
    def m1(self):
        print("inside m1")

class p2(p1):
    def m2(self):
        print("inside m2")

class p3(p2):
    def m3(self):
        print("inside m3")

p3=p3()
p3.m3()
p3.m2()
p3.m1()


#multiple inheritance
class p1:
    def m1(self):
        print("inside m1")


class p2():
    def m2(self):
        print("inside m2")


class p3(p2,p1):
    def m3(self):
        print("inside m3")

p3 = p3()
p3.m3()
p3.m2()