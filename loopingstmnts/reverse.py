
num=123
res=""

while(num != 0):
    lastdigit=num % 10
    # print(lastdigit,end="")
    res=res+str(lastdigit)
    num=num // 10
print(res)

