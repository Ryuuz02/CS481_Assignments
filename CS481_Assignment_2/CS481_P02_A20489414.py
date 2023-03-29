title_lst = []
tag_lst = []
from nltk import PorterStemmer
stemmer = PorterStemmer()

with open(r"CS481_Assignment_2/dataset.csv", "r", encoding="utf8") as f:
    while True:
        entry = f.readline()
        if entry != "":
            title = ""
            if entry[-8:] == "Liberal\n":
                split_title = entry[:-9].split(" ")
                tag_lst.append("liberal")
                
            else:
                split_title = entry[:-14].split(" ")
                tag_lst.append("conservative")

            for word in split_title:
                word = word.replace(",", "")
                title += stemmer.stem(word) + " "
            title_lst.append(title)
        else:
            break
        
        

with open(r"CS481_Assignment_2/PreProcessed.csv", "a", encoding="utf8") as f:
    for i in range(len(title_lst)):
        f.write(title_lst[i] + "\n")
        f.write(tag_lst[i] + "\n")

print("Preprocessing Done!")