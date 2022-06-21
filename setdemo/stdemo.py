# st={12,4,11,16,17,17,17,12,5}
# print(st)
#
#
# st1={1,2,3,4,5}
# st2={10,11,12,2,3}
# st1.add(10)

# union_set=st1.union(st2)
# print(union_set)
#
# inter_set=st1.intersection(st2)
# print(inter_set)
#
# diff_set=st1.difference(st2)
# print(diff_set)
# st3={100,200,300}


students=["ram","ravi","hari","tom","nikil","jain","john"]
st1=set(students)
passed_st=["ravi","hari","tom"]
st2=set(passed_st)
failed_st=st1-st2
print(failed_st)

fail_st=set(students).difference(set(passed_st))
print(fail_st)


