#lambda function


cube=lambda n:n**3
print(cube(3))

maxtwo=lambda num1,num2:num1 if num1>num2 else num2
print(maxtwo(5,8))

# def max_two(n1,n2):
#     return n1 if n1>n2 else n2
# print(max_two(4,5))



sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(sub(2,4))

add=lambda  n1,n2: n1+n2
print(add(10,20))

div=lambda n1,n2:n1/n2
print(div(10,5))

mul=lambda n1,n2:n1*n2
print(mul(2,3))


def range_sum(low,upp):
    return sum(range(low,upp))
print(range_sum(10,50))

rng=lambda low,upp:sum(range(low,upp))
print(rng(10,50))
