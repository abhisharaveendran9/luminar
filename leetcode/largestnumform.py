from functools import reduce

# lst=[3,30,34,5,9]
# str_lst=[str(n) for n in lst]
# max_num=reduce(lambda n1,n2: (n1+n2) if (n1+n2)>=(n2+n1) else (n2+n1),str_lst)
# print(max_num)


lst=[9,39,8,78]
str_lst=[str(n) for n in lst]
str_lst=sorted(str_lst,reverse=True)
out=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>=(n2+n2) else (n2+n1),str_lst)
print(out)