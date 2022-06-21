accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]

#q1 print deatils of 1002
# for ac in accounts:
#     if ac["acno"]==1002:
#         transactions=ac.pop("transactions")
#         print(ac)

#ac_details=[ac["acno"] for ac in accounts if ac["acno"]==1002]
#print(ac_details)


#q2
#savings_type= [ ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
#print(savings_type)

#q3
#accounts.sort(reverse=True,key=lambda  ac:ac["balance"])
#print(accounts)




#all_trans=[ac["transactions"] for ac in accounts]

#q4 prit all phone pay transactions

#phpay=[trans for tlist in all_trans for trans in tlist if trans["method"]=="phone-pay"]
#print(phpay)

#q4 prit all transactions where transaction amount > 500

#stmt_gt_fi=[trans for tlist in all_trans for trans in tlist if trans["amount"]>500]
#print(stmt_gt_fi)


#q5 crredit transactions of 1002

#credit_trans=[trans for tlist in all_trans for trans in tlist if trans["to"]==1002]
#print(credit_trans)


#q6 aggregate transactions based on payment mode

pms={} #empty dict
all_trans=[ac["transactions"] for ac in accounts]
transactions=[t for tlist in all_trans for t in tlist ]
#for t in transactions:
 #   print(t)
for transaction in transactions:
    p_method=transaction["method"]
    p_amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=p_amount
    else:
        pms[p_method]=p_amount

print(pms)


print(max(pms.items(), key=lambda itm:itm[1]))  #highest payment
#print(all_trans)