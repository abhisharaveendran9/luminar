#word count

text="hai hello hai hello"

words=text.split(" ")
print(len(words))

#hai:2 hello:2

word_count={}  #hai:2 hello:2
for w in words: #w="hello"

    if w in word_count:  #hllo in wcount
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)