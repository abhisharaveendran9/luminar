              #*args     #print as tuple
# def add(*args):
#     return sum(args)
# print(add(10,20))
# print(add(10,20,30))
#
#
# def max_fun(*args):
#     return max(args)
# print(max_fun(12,13,15,10,11,100))
#
# def min_fun(*args):
#     return min(args)
# print(min_fun(19,14,10,11,12))


           #**kwargs

def print_details(**kwargs):   #print as dict
    print(kwargs)
print_details(name="arjun",wplace="kochi",nplace="thsr")  #o/p: {'name': 'arjun', 'wplace': 'kochi', 'nplace': 'thsr'}



def add_nums(**kwargs):
    print(sum([v for k,v in kwargs.items()]))   #70
    print(sum([v for v in kwargs.values()]))    #70
add_nums(n1=10,n2=20,n3=40)