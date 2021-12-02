'''
This is not the tfidf implementation just a way to build a vocabulary of unique words
probably a better solution using hash tables?
'''



import re
d1 = "You say goodbye, I say hello"
d2 = "You say stay, I say go"
d3 = "Hello, hello, I say go"
d4 = "I say yes, you say no"

def remove_punctuation(str):
    return re.sub('[^A-Za-z0-9\s]', '', str)


d1 = remove_punctuation(d1)
d2 = remove_punctuation(d2)
d3 = remove_punctuation(d3)
d4 = remove_punctuation(d4)

# make lower case and store as array
d1 = d1.lower().split(' ')
d2 = d2.lower().split(' ')
d3 = d3.lower().split(' ')
d4 = d4.lower().split(' ')

# get all the unique words in an arbitrary number of docs
def get_vocabulary(*argv):
    v = []
    for arg in argv:
        for word in arg:
            if word not in v:
                v.append(word)
    return v

v = get_vocabulary(d1,d2,d3,d4)  

v
len(v)