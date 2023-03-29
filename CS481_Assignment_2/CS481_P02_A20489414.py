title_lst = []
tag_lst = []
from nltk import PorterStemmer
from time import sleep
stemmer = PorterStemmer()


with open(r"CS481_Assignment_2/dataset.csv", "r") as f:
    #Title Line
    f.readline()

    entry = f.readline()[1:]
    count = 0
    letter = 0
    while count != 1:
        if entry[letter:letter+9] == '",Liberal' or entry[letter:letter+14] == '", Conservative':
            count += 1
        letter += 1
    title = entry[:letter-1]
    split_title = title.split(" ")
    for word in split_title:
        word.replace(",", "")
        stemmer.stem(word)

    count = 0
    letter2 = letter
    while count != 2:
        if entry[letter2] == ',':
            count += 1
        letter2 += 1
    tag = entry[letter+1:letter2-1]

    title_lst.append(title)
    tag_lst.append(tag)

with open(r"CS481_Assignment_2/PreProcessed.csv", "w") as f:
    for i in range(len(title_lst)):
        f.write(title_lst[i])
        f.write(tag_lst[i])
