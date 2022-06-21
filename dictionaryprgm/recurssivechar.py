pattern="ABAACCD"

#print first recurssive character

#w_count={}
# for l in pattern:
#     if l in w_count:
#         w_count[l]+=1
#     else:
#         w_count[l]=1
# print(w_count)

char_count={}

for char in pattern:
    if char in char_count:
        print(f"first recursive character is {char}")
        break
    else:
        char_count[char]=1


#second recursive character
#pattern="ABAACDA"
char_count={}
recc_char=[]#list

for char in pattern:
    if char in char_count:
        recc_char.append(char)
    else:
        char_count[char]=1
print(recc_char,"scnd recursive char")


#most rec

person=[
    ["ram",45],
    ["rav",55],
    ["raj",35],
    ["akk",46]
]
print(sorted(person,key=lambda p:p[1],reverse=False))
#sorting dictionary based on value

words_count={"a":2,"b":3,"c":2,"d":4,"e":2}
print(max(words_count.items(),key=lambda i:i[1])) #max applying to dict
print(min(words_count.items(),key=lambda m:m[1])) #min to dict,dict is not indexing so here using item to find

wc_list=words_count.items() #wc_list=([('a', 2), ('b', 3), ('c', 2), ('d', 4), ('e', 2)])
print(sorted(wc_list,key=lambda item:item[1], reverse=True))

print(max(wc_list,key=lambda item:item[1]))#dict to list ,max



#iterating dicts
# for k in words_count:
#     print(k)

# for k,v in words_count.items():
# #    print(k,v)
# print(words_count.items())


#sum,max,min

#print("sort" in dir(dict))
#print(dir(dict))

#print(sorted(words_count)) #sort based on keys here


