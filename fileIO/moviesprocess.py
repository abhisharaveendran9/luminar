
allmovies=[]
mread=open("movies.txt","r")
for movie in mread:
    #print(movie)
    mov=movie.rstrip("\n").split(",")
    allmovies.append(mov)
print(allmovies)


# number of moviews released in 2022
num_mov=[movs for movs in allmovies if movs[1]=="2022" ]
print(num_mov)

# number malayalam movies
malayalam=[movs for movs in allmovies if movs[3]=="malayalam"]
print(malayalam)

# theater released movies
theater=[movs for movs in allmovies if movs[-1]=="theater"]
print(theater)

# list of movies whose rating > 5
rating=[mov for mov in allmovies if mov[2]>="5"]
print(rating)

movie_out={}
for movies in allmovies:
    year=movies[1]
    if year in movie_out:
        movie_out[year]+=1
    else:
        movie_out[year]=1
print(movie_out)
print(movie_out.items())
out=max(movie_out.items(),key=lambda ite:ite[1])
print(out)


#dict= {2022:,4,2021:6,2020:2}
# 20210