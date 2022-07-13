import json
import random
try:
    with open("../blogjsons/users.json") as f:
        data=json.load(f)
        print(data)
    all_users=[user["id"] for user in data]
    my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]
    my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
    to_follow=set(all_users)-set(my_followings)
    to_follow.remove(my_id)
    print(to_follow)
    suggestions=random.sample([*to_follow],2)
    print(suggestions)

except Exception as e:
    print(e.__class__)

#destructuring  # set converted to a list
st=[12,11,10,4,5,5,3,1]
lst=[*st]
print(lst)

lsts=[1,3,2,5,6,5] #list to set
sts={*lsts}
print(sts)
