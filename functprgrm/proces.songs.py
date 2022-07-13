import  functools

#q1 print total number of songs in album1
import json
import random

with open("songs.json",encoding="utf-8") as f:
    data=json.load(f)
# num_song=[song for song in data if song["album"]=="album1"]
# print(len(num_song))
#
# albu_sng_count=list(filter(lambda song:song["album"]=="album1",data))
# print(len(albu_sng_count))
#
# #highest rating song
# top_songs=max(data,key=lambda s:s["rating"])
# print(top_songs["rating"])
# highest_rating=[song for song in data if song["rating"]==top_songs["rating"]]
# print(highest_rating)
#
# t_songs=functools.reduce(lambda s1,s2:s1 if s1["rating"] > s2["rating"] else s2,data)
# print(t_songs)



#sad mode songs with random sample of 2

sad_song=[s for s in data if s["mode"]=="sad"]
# print(random.sample(sad_song,2))


#total number of albums

total_albums=set([s["album"] for s in data])
# print(len(total_albums))


#wich album containg most songs
song_count={} #dictionary
for song in data:
    album_name=song.get("album")   #album1
    if album_name in song_count:
        song_count[album_name]+=1
    else:
        song_count[album_name]=1
print(song_count)

print(max(song_count.items(),key=lambda s:s[1]))