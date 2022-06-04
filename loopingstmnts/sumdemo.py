# sum of numbers
# 2 =2+22= 24
# 3  =3+33+333= 369
# 4=4+44+444+4444= 4936


num=3
i=1
res=""
sum=0

while(i<=num):
    res=res+str(num)  #i=2
    sum=sum+int(res)
    i+=1
print(sum)
