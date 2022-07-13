fread=open("mobile.txt","r")
all_mobiles=[]
for line in fread:
    mobile=line.rstrip("\n"). split(",")
    all_mobiles.append(mobile)
print(all_mobiles)
# all_mobiles=[mobile.rstr]


costly_mobile=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mobile)

fmob=[mob for mob in all_mobiles if mob[3]=="5g"]
print(fmob)

dmob=[mob for mob in all_mobiles if mob[-1]=="lcd"]
print(dmob)