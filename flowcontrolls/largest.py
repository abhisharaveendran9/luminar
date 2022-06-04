num1=10
num2=20
num3=180
# if(num1>num2):
#     print("num1 is largest")
# else:
#     print("num2 is largest")

# print(num1 if num1>num2 else num2)

#largest amoung 3 numbers

if (num1>num2) and (num1>num3):
    print("num1 is largest")
elif (num2>num1) and (num2>num3):
    print("num2 is largest")
elif(num3>num1) and (num3>num2):
    print("num3 is largest")
else:
    print("same")
