#1234
#1234
#1234

# for raw in range(1,5):
#     for col in range(1,5):
#         print(raw,end=" ")
#     print()


# for raw in range(1,5):
#     for col in range(1,5):
#         if(raw>=col):
#             print(col,end="   ")
#     print()


#1
#2 2
#3 3 3
#4 4 4 4

# for raw in range(1,5):
#     for col in range(1,raw+1):
#        print(raw,end=" ")
#     print()

# for raw in range(1,5):
#    for col in range(1,raw+1):
#         print("#",end=" ")
#     print()


# for r in range(1,5):
#     for c in range(5,r,-1):
#         print("#",end="\t")
#     print()


# n=7  # triangle pyramid
# for r in range(n):
#     for c in range(n-r-1):
#         print(" ",end=" ")
#     for k in range(2*r+1):
#         print("*",end=" ")
#     print()













n=7

for r in range(1,7):

    for c in range(1,(r+1)):
        print(" ",end="")
    for s in range(1, (7 - r)):
        print(" ", end=" ")
    print()










# n=5 #reverse pyramids
# for r in range(n):
#     for c in range(r):
#         print(" ",end=" ")
#     for k in range(2*(n-r)-1):
#         print("*",end=" ")
#     print()






# # hollow pyramid star pattern
# n = 5
# for i in range(n):
#     # printing spaces
#     for j in range(n - i - 1):
#         print(' ', end='')
#
#     # printing stars
#     for k in range(2 * i + 1):
#         # print star at start and end of the row
#         if k == 0 or k == 2 * i:
#             print('*', end='')
#         else:
#             if i == n - 1:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#     print()