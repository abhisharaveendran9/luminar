#file input output


# f=open("abc.txt","r)

# ls=[]
# for line in f:
#     #print(line)
#     ls.append(line)
# print(ls) # to list the op

#lines=list(f)
#print(lines)

# to remove \n -> ['hai hello\n', 'hello world\n', 'hello hai hello']
# out=[line.rstrip("\n") for line in f]
# print(out)


f=open("abc.txt","w")
#
# # company_name="luminar"
# # f.write(company_name)
lst=["python","javascript","c#"]
for lan in lst:
    lan+="\n"
    f.write(lan)
