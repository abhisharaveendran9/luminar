class course:
    course_name=str
    active_status=bool

    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")


    def __str__(self):
        return self.course_name



class batch:
    course:course
    batch_code:str
    start_date:str

    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code

class student:
    student_name:str
    gender:str
    rol:str
    batch:str

    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.rol=kwargs.get("roll")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name



django=course()
django.add_course(course_name="django",active_status="True")
# print(django)
bigdat=course()
bigdat.add_course(course_name="bigdat",active_status="True")
# print(bigdat)

db1=batch()
db1.add_batch(course=django,batch_code="djmay2k22",start_date="5-6-2022")
# print(db1)
bd1=batch()
bd1.add_batch(course=bigdat,batch_code="bdmay2k22",start_date="5-6-2022")
# print(bd1)

rahul=student()
rahul.add_student(student_name="rahul",gender="male",roll="2345",batch=db1)

akshay=student()
akshay.add_student(student_name="akshay",gender="male",roll="2346",batch=db1)

nikil=student()
nikil.add_student(student_name="nikil",gender="male",roll="2347",batch=bd1)

hayan=student()
hayan.add_student(student_name="hayan",gender="male",roll="2348",batch=bd1)

# print(rahul.batch.course.course_name)






master_word="abbcceddffggt"
wr=list(master_word)
print(wr)
chk_word="egg"
chk=list(chk_word)
print(chk)

# for wr in master_word:
#     for chk in chk_word:
#         if(wr==chk):
#             print("ok")

num=[9,39,8,78]
#largest number
# print(sorted(num))
lst=sorted(num)
# print(lst)