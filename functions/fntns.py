#print
#range
#type
#sum

# def sum_numbers(n1,n2):
#     return n1+n2
# print(sum_numbers(10,20))
#
#
# def sub_numbers(n1,n2):
#     return n1-n2
# print(sub_numbers(10,5))
#
#
# def smart_check(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# print(smart_check(10,15))
#
# def num_check(n1):
#     return "even" if n1%2==0 else "odd"
# print(num_check(5))


# def validate_gmail(email):
#     return email.endswith("@gmail.com")
# print(validate_gmail("abcd@gmail.com"))
#
# #factorial of a given number
#
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact
# print(factorial(3))



def prime(num):
    flag=0
    for i in range(2, num):
        if (num % i == 0):
            flag = 1
            break
    return flag==0
print(prime(3))


def prime_range(low,upp):
    for num in range(low,(upp+1)):
        if prime(num):
            print(num)
prime_range(10,20)
