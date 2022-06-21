lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]
#print all nos >16
# for sub_list in lst:
#     for num in sub_list:
#         if num>16:
#             print(num)

# flatten_list=[]
# for sub_list in lst:
#     for num in sub_list:
#         flatten_list.append(num)
# print(max(flatten_list))

# fln_list=[num for sub_lst in lst for num in sub_lst]
# print(fln_list)
#
# num_g_sixt=[num for num in fln_list if num>16]
# print(num_g_sixt)
#
# oddsum=sum([num for num in fln_list if num%2!=0])
# print((oddsum))
#
# num_even= [num for num in fln_list if num%2==0]
# print(sum(num_even))

fltn_list=[num for slist in lst for num in slist]
mapped_lst=[num+1 if num>25 else num-1 for num in fltn_list]
print(mapped_lst)