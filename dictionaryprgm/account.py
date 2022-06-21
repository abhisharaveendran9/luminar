

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


mobile={
    "mobile_name":"redminote12pro",
    "display":"led",
    "price":45000,
    "ram":"6gb",
    "memory":"64gb"
}

#dict_name.get(key)

print(mobile.get("mobile_nam"))
print(mobile.get("ram"))
print(mobile.get("memory"))
print("db transaction")

mobile["band"]="5g" if "band" in mobile else "4g"
print(mobile)

#mobile price update c_price-1000 if cur_price > 40000 else c_price-500

if mobile["price"]>40000:
    mobile["price"]-=1000
else:
    mobile["price"]-=500
print(mobile)