class user:
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

class AddProduct:

    def post(self,**kwargs):
        ur=kwargs.get("user")

        if ur.role=="admin":
            self.product_name=kwargs.get("p_name")
            self.user=kwargs.get("user")
        else:
            print("no privillage")

user=user(name="abhi",role="customer")

pro1=AddProduct()
pro1.post(p_name="laptop",user=user)