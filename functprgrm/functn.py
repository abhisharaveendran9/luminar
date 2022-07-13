#map
#filter
#reduce
from functools import reduce

lst=[10,2,30,4]
sqares=list(map(lambda n:n**2,lst))
cubes=list(map(lambda  n:n**3,lst))


num_out=list(map(lambda n:n-1 if n<2 else n+1,lst))
print(num_out)

#reduce
sum=reduce(lambda  n1,n2:n1+n2,lst)
print(sum)

all_product=reduce(lambda n1,n2:n1*n2,lst)
print(all_product)

maximum=reduce(lambda  n1,n2:n1 if n1>n2 else n2,lst)
print(maximum)

minimum=reduce(lambda  n1,n2:n1 if n1<n2 else n2,lst)
print(minimum)