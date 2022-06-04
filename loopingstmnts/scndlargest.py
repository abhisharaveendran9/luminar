num1=2
num2=4
num3=3

if(num1>=num2) and (num1>=num3):
    if(num2>=num3):
        print("num2 is second largest")
    else:
        print("num3 is largest")
elif(num2>=num1) and (num2>=num3):
    if(num1>=num3):
        print("num1 is largest")
    else:
        print("num3 is largest")
elif(num1>=num2):
    print("num1 is second largest")
else:
    print("num2 is second largest")

