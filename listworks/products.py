mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
#flatn_list=[mobile for sub_list in mobiles for mobile in sub_list]
#print(flatn_list)

#total no of mobiles
#print(f"total no of mobiles= {len(mobiles)} ")

# q1 total number of out_of_stock mobiles
#outof_stk= [mobile for mobile in mobiles if mobile[6]==0]
#print(f"total no of out of stock mobiles={outof_stk}")

# q2 total stock
#total_stk= [mob[-1] for mob in mobiles]
#print(sum(total_stk))

# q3 print mobiles available in range 20k to 30k
#availablemob= [mob for mob in mobiles if mob[4]>=20000 and  mob[4]<=30000]
#print(len(availablemob), availablemob)


# q4 print all 5g phone
#fiveg_mob=[mob for mob in mobiles if mob[2]=="5g"]
#print(len(fiveg_mob),fiveg_mob)

# q5 print samsung mobiles
#samsng_mob=[mob for mob in mobiles if mob[1]=="samsung"]
#print(len(samsng_mob), samsng_mob)

# q6 print costly mobile

#costly_mob=max(mobiles, key=lambda mob:mob[4])
#print(costly_mob)


# highcost=[mob[4] for mob in mobiles] #print only price
# print(max(highcost))

#mobiles.sort(reverse=True,key=lambda mob:mob[4])


# q7 prin low cost mobiles
#low_cost=min(mobiles, key=lambda  mob:mob[4])
#print(low_cost)

# lowcst=[mob[4] for mob in mobiles]
# print(min(lowcst))

# q8 print all mobiles having stock >10
#stks=[mob for mob in mobiles if mob[6] > 10]
#print(stks)

# q9 count of mobiles having dispaly amoled
#displays=[mob for mob in mobiles if mob[3]=="AMOLED"]
#print(len(displays))

# q10 sort mobiles based on price order by desc
# price=[mob[4] for mob in mobiles]
# price.sort(reverse=True)
# print(price)

mobiles.sort(reverse=True,key=lambda mob:mob[4])
print(mobiles)

# q11 sort mobiles based on avl stock oredr by desc
# stock=[mob[-1] for mob in mobiles]
# stock.sort(reverse=True)
# print(stock)

mobiles.sort(reverse=True,key=lambda mob:mob[-1])
print(mobiles)

# q12 is there any mobile available at rs 10000 ?
#mob_ten=[True for mob in mobiles if mob[4]==10000]
#print(mob_ten)

#mob_ten= [mob[4]==10000 for mob in mobiles]
#print("available" if True in mob_ten else "Na")

# q12 list all mobiles having same price






# list=[1,2,4,21,43,16,12,90,17760,98,94,11]
# list.sort(reverse=True)
# print(list)
#
# li=[[5,6],[88,9],[3,1]]
# li.sort(reverse=True)
# print(li)