
# account={
#         "acno":1000,
#          "opening_date":"12-01-2010",
#          "type":"savings",
#          "pname":"ram"
#          }

# print(account["acno"])
# print(account["pname"])
#
# print("balance" in account)
# account["balance"]=5000
# print(account)
#
# account["balance"]+=1000
# print(account)


# mobile={
#     "mobile_name":"redminote12pro",
#     "display":"led",
#     "price":45000,
#     "ram":"6gb",
#     "memory":"64gb"
# }
#
# #dict_name.get(key)  #get is using if there is no op thn prints None only not errors
#
# print(mobile.get("mobile_nam"))
# print(mobile.get("ram"))
# print(mobile.get("memory"))
# print("db transaction")
#
# mobile["band"]="5g" if "band" in mobile else "4g"
# print(mobile)
#
# #mobile price update c_price-1000 if cur_price > 40000 else c_price-500
#
# if mobile["price"]>40000:
#     mobile["price"]-=1000
# else:
#     mobile["price"]-=500
# print(mobile)





results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]

#sorted list based on win
print(sorted(results,key=lambda res:res["win"],reverse=True))

#print district with minimum win
print(min(results,key=lambda res:res["win"]))

#sort results based on A+
print(sorted(results,key=lambda res:res["A+"],reverse=True))

#print dist with low count A+
print(min(results,key=lambda res:res["A+"]))

#print total no of students who got full A+
aplus=[res["A+"] for res in results]
print(aplus)