#searching an element from an array


arr=[1,2,3,13,14,15,16,65,78,89]
element=15
flag=0

# for num in arr:
#     if (num==element):
#         flag=1
#         break
# if flag==1:
#     print(f"element is found, position {arr.index(element)}")
# else:
#     print("not found")

# for i in range(0,len(arr)):
#     if element==arr[i]:
#         flag=1
#         break
# print("element found" if flag!=0 else "not found")


lst=[10,11,12,14,15,16,17,12,12,75,89,100]

print(lst.count(12))

oddlist=[]

for num in lst:
    if num%2!=0:
        oddlist.append(num)
print(oddlist)
oddlist.sort(reverse=True)
print(oddlist)

evenlist=list() #class name, object created

for num in lst:
    if num%2==0:
        evenlist.append(num)
print(evenlist)