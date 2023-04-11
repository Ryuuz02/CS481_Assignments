from nltk import PorterStemmer
stemmer = PorterStemmer()

with open(r"CS481_Assignment_2/Vocabulary.txt", "r", encoding="utf8") as f:
    vocabulary = set(f.read().split("<s>"))

train_title_list = []
train_tag_list = []
with open(r"CS481_Assignment_2/Titles.csv", "r", encoding="utf8") as f1:
    with open(r"CS481_Assignment_2/Tags.csv", "r", encoding="utf8") as f2:
        # Read 4/5 of lines
        counter = 0
        while True:
            title = f1.readline()
            tag = f2.readline()
            if title != "":
                if counter % 5 != 0:
                    train_title_list.append(title[:-2])
                    train_tag_list.append(int(tag))
                counter += 1
            else:
                break


conservative_probability = sum(train_tag_list) / len(train_tag_list)
liberal_probability = 1 - conservative_probability
liberal_probability_dict = {}
conservative_probability_dict = {}
word_count = {}

for word in vocabulary:
    word_count[word] = 1
    liberal_probability_dict[word] = 1
    conservative_probability_dict[word] = 1

for i in range(len(train_title_list)):
    split_title = set(train_title_list[i].split(" "))
    for word in split_title:
        word_count[word] += 1
        if train_tag_list[i] == 0:
            liberal_probability_dict[word] += 1
        else:
            conservative_probability_dict[word] += 1

def calculate_probability_input():
    title = input("Enter your sentence: ")
    print("\nSentence S:\n" + title + "\n")
    global stemmer
    split_title = title.split(" ")
    stemmed_title = set()
    for word in split_title:
        word = stemmer.stem(word.replace(",", ""))
        stemmed_title.add(word)
    lib_prob = liberal_probability
    con_prob = conservative_probability
    for word in stemmed_title:
        if word in vocabulary:
            lib_prob *= liberal_probability_dict[word] / word_count[word]
            con_prob *= conservative_probability_dict[word] / word_count[word]
    if lib_prob > con_prob:
        print("was classified as liberal")
    else:
        print("was classified as conservative")
    print("P(Liberal|S) = " + str(lib_prob))
    print("P(Conservative|S) = " + str(con_prob))

def calculate_probability(title):
    global stemmer
    split_title = title.split(" ")
    stemmed_title = set()
    for word in split_title:
        word = stemmer.stem(word.replace(",", ""))
        stemmed_title.add(word)
    lib_prob = liberal_probability
    con_prob = conservative_probability
    for word in stemmed_title:
        if word in vocabulary:
            lib_prob *= liberal_probability_dict[word] / word_count[word]
            con_prob *= conservative_probability_dict[word] / word_count[word]
    if lib_prob > con_prob:
        return 0
    else:
        return 1


    
    

