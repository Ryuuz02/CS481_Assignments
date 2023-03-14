import nltk
import re
import operator

# nltk.download("brown")

sent_end = [".", "?", "!"]
brown = nltk.corpus.brown
brown_words = list(brown.words())
lower_brown = [x.lower() for x in brown_words]
brown_dict = {}
for i in range(len(lower_brown) - 1):
    word = lower_brown[i]
    if word not in sent_end and lower_brown[i+1] not in sent_end:
        if word not in brown_dict.keys():
            brown_dict[word] = [lower_brown[i+1]]
        else:
            brown_dict[word].append(lower_brown[i+1])
user_sentence = input("Please enter a sentence (don't include .!?):\n").lower()
words = re.split("[;, ]+", user_sentence)
bigrams = []
for i in range(len(words) + 1):
    if i == 0:
        bigrams.append(["<s>", words[0]])
    elif i == len(words):
        bigrams.append([words[i - 1], "<s>"])
    else:
        bigrams.append([words[i-1], words[i]])
probability = 1
extended_bigrams = bigrams
for i in range(len(bigrams)):
    bigram = bigrams[i]
    word1 = bigram[0]
    word2 = bigram[1]
    if "<s>" in bigram:
        bigram_probability = 0.25
    else:
        try:
            followup = brown_dict[word1]
            if word2 in followup:
                bigram_probability = operator.countOf(followup, word2) / len(followup)
            else:
                bigram_probability = 0
        except KeyError:
            bigram_probability = 0
    extended_bigrams[i].append(bigram_probability)
    probability *= bigram_probability
print(extended_bigrams)
print("Total Probability of Sentence: " + str(probability))
