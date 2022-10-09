#print(dir(list)) all methods in list

# list1=[10,11,12,13,14,15]
#
# flag=0
# element=15
#
# for num in list1:
#     if element==num:
#         flag=1
#         break
# print("found" if flag>0 else "not found")     #linear search


arr=[10,11,12,13,14,15,16]

flag=0
element=15

arr.sort()  #binarysearch ,sort list
low=0
upp=len(arr)-1
while(low<=upp):
    mid=(low+upp)//2
    if element==arr[mid]:
        flag=1
        break
    elif element>arr[mid]:
        low=mid+1
    elif element<arr[mid]:
        upp=mid-1
print("found" if flag>0 else "not found")