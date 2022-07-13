import json

with open("blogs.json",encoding="utf-8")as f:
    data=json.load(f)
    print(data)

print(len(data)) #count od data in list

#number of post by userId=1
post_user=[post for post in data if post["userId"]==1]
print(len(post_user))

#total number of likes for postId 6
num_likes=[len(post["liked_by"]) for post in data if post["postId"]==6 ]
print(num_likes)

#number of post liked by user= 2
num_like_user=len([post for post in data if 2 in post["liked_by"]])
print(num_like_user)