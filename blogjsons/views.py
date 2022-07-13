#AUTHENTICATION LOGIN

from blogjsons.models import users,posts

#print(users)

#username="akhil"
#password="password@123"

session={}

def sighin_required(fn):  #DECORATOR fn  if user is login or not, it stored in session as a dictionary
    def wrapper(*args,**kwargs): #deco method
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session you must login")
    return wrapper

def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user

#print(authenticate(username="akhil",password="Password@123"))

class LoginView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
       # print(session)

class PostListView:
    @sighin_required
    def get(self,*args,**kwargs):
        return posts

    @sighin_required
    def post(self,*args,**kwargs):
        #print(kwargs)
        #my_post=kwargs.get("data")
        userId=session["user"]["id"]
        my_post["userId"]=userId
        posts.append(my_post)
        print(posts[-1])



class MyPostListView:
    @sighin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post

class AddLike:
    @sighin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])

log_in=LoginView()
log_in.post(username="richard",password="Password@123")

all_post=PostListView()
my_post = {
    "title": "hello good morning", "content": "mycontent", "liked_by": []
}

all_post.post(data=my_post)

like=AddLike()
like.post(postid=1)
# all_post=PostListView()
# print(all_post.get())
#
# myposts=MyPostListView()
# print(myposts.get())