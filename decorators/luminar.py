# class staff(object):
#     id:int
#     name:str
#     role:str
#
#     def __init__(self,*args,**kwargs):
#         self.id=kwargs.get("id")
#         self.name=kwargs.get("name")
#         self.role=kwargs.get("role")
#
#     def __str__(self)->str:
#         return self.name
#         #return str(self.id)
#
# user=staff(id=100,name="rahul",role="admin")
# print(user)




class employee:

    def __init__(self,**kwargs):
        self.eid=kwargs.get("eid")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name

emp=employee(eid="101",name="rahul",role="admin")
print(emp)

class department():

    def __init__(self,**kwargs):
        user=kwargs.get("user")
        if user.role=="admin":
            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("no access")

    def __str__(self):
        return self.dept_name

dept=department(dept_name="django",user=emp)
print(dept)