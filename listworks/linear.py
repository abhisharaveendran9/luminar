#linear searching

# lst1=[10,11,12,13,14]
# lst2=[11,14,15,16,17]
# lst3=[]
#
# for num in  lst1:
#     if num in lst2:
#         lst3.append(num)
# print(lst3)

dup_list=[]

lst1=[10,11,11,12,13,14,14,14]
for i in range(0,len(lst1)):
    for j in range((i+1),len(lst1)):
        if lst1[i]==lst1[j]:
            dup_list.append(lst1[i])
print(dup_list)
#print(f"first occurent {i},most occurent {j}")