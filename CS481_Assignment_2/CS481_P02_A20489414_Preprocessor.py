from nltk import PorterStemmer
stemmer = PorterStemmer()

def preprocess(ignore=False):
    global stemmer
    vocabulary = set()
    title_lst = []
    tag_lst = []
    if not ignore:
        from nltk import corpus
        stops = corpus.stopwords.words("english")
        # filtered_brown = [w for w in brown_words if w.lower() not in stops]
    with open(r"CS481_Assignment_2/dataset.csv", "r", encoding="utf8") as f:
        while True:
            entry = f.readline()
            if entry != "":
                title = ""
                if entry[-8:] == "Liberal\n":
                    split_title = entry[:-9].split(" ")
                    tag_lst.append(0)
                    
                else:
                    split_title = entry[:-14].split(" ")
                    tag_lst.append(1)

                for word in split_title:
                    if not ignore:
                        if word.lower() not in stops:
                            word = stemmer.stem(word.replace(",", ""))
                            if word not in vocabulary:
                                vocabulary.add(word)
                            title += word + " "
                    else:
                        word = stemmer.stem(word.replace(",", ""))
                        if word not in vocabulary:
                            vocabulary.add(word)
                        title += word + " "
                title_lst.append(title)
            else:
                break
            
            

    with open(r"CS481_Assignment_2/Titles.csv", "w", encoding="utf8") as f1:
        with open(r"CS481_Assignment_2/Tags.csv", "w", encoding="utf8") as f2:
                for i in range(len(title_lst)):
                    f1.write(title_lst[i] + "\n")
                    f2.write(str(tag_lst[i]) + "\n")

    with open(r"CS481_Assignment_2/Vocabulary.txt", "w", encoding="utf8") as f:
        for word in vocabulary:
            f.write(word + "<s>")