import listworks.search


class parent:
    def phone(self):
        print("nokia")
    def bike(self):
        print("passion pro")

class child(parent):
    def phone(self):
        print("iphone")
    def bike(self):
        print("duke")

ch=child()
ch.phone()
ch.bike()


#super method
class parent:
    def properties(self):
        self.props = {"mobile":"nokia", "bike":"passion pro"}
        return  self.props

class child(parent):
    def properties(self):
        props= super().properties()
        props["car"]="swift"
        return props

ch=child()
print((ch.properties()))

list.append()