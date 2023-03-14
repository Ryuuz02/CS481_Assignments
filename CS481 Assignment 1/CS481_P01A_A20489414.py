import nltk
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('brown')
nltk.download('reuters')
nltk.download('twitter_samples')

stops = nltk.corpus.stopwords.words("english")

brown = nltk.corpus.brown
brown_words = brown.words()
filtered_brown = [w for w in brown_words if w.lower() not in stops]
brown_frequency = nltk.FreqDist(word.lower() for word in filtered_brown)
brown_freq_dict = {}
for word in filtered_brown:
    brown_freq_dict[word] = brown_frequency[word]

reuters = nltk.corpus.reuters
reuters_words = reuters.words()
filtered_reuters = [w for w in reuters_words if w.lower() not in stops]
reuters_frequency = nltk.FreqDist(word.lower() for word in filtered_reuters)
reuters_freq_dict = {}
for word in filtered_reuters:
    reuters_freq_dict[word] = reuters_frequency[word]
#
twitter_sample = nltk.corpus.twitter_samples
twitter_sample_str = twitter_sample.strings()
twitter_sample_words = []
for i in range(len(twitter_sample_str)):
    for word in twitter_sample_str[i].split():
        twitter_sample_words.append(word)
filtered_twitter_samples = [w for w in twitter_sample_words if w.lower() not in stops]
twitter_samples_frequency = nltk.FreqDist(word.lower() for word in filtered_twitter_samples)
twitter_samples_freq_dict = {}
for word in filtered_twitter_samples:
    twitter_samples_freq_dict[word] = twitter_samples_frequency[word]

sorted_brown = sorted(brown_freq_dict, key=brown_freq_dict.get, reverse=True)
top_1000_brown_freq = [brown_freq_dict[f] for f in sorted_brown[:1000]]
sorted_reuters = sorted(reuters_freq_dict, key=reuters_freq_dict.get, reverse=True)
top_1000_reuters_freq = [reuters_freq_dict[f] for f in sorted_reuters[:1000]]
sorted_twitter = sorted(twitter_samples_freq_dict, key=twitter_samples_freq_dict.get, reverse=True)
top_1000_twitter_freq = [twitter_samples_freq_dict[f] for f in sorted_twitter[:1000]]
print("10 most common for Brown:")
print(sorted_brown[:10])
print("10 most common for Reuters:")
print(sorted_reuters[:10])
print("10 most common for Twitter:")
print(sorted_twitter[:10])
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot(range(1000), top_1000_brown_freq)
ax1.set_title("Brown")
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xlabel("Log(Rank)")
ax1.set_ylabel("Log(Frequency)")

ax2.plot(range(1000), top_1000_reuters_freq)
ax2.set_title("Reuters")
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlabel("Log(Rank)")
ax2.set_ylabel("Log(Frequency)")

ax3.plot(range(1000), top_1000_twitter_freq)
ax3.set_title("Twitter")
ax3.set_xscale("log")
ax3.set_yscale("log")
ax3.set_xlabel("Log(Rank)")
ax3.set_ylabel("Log(Frequency)")

plt.show()

tech_uni = "genetics"
nontech_uni = "clear"

try:
    print("Frequency of " + tech_uni + " in brown: " + str(brown_freq_dict[tech_uni]))
except KeyError:
    print("Frequency of " + tech_uni + " in brown: 0")
try:
    print("Frequency of " + nontech_uni + " in brown: " + str(brown_freq_dict[nontech_uni]))
except KeyError:
    print("Frequency of " + nontech_uni + " in brown: 0")
try:
    print("Frequency of " + tech_uni + " in reuters: " + str(reuters_freq_dict[tech_uni]))
except KeyError:
    print("Frequency of " + tech_uni + " in reuters: 0")
try:
    print("Frequency of " + nontech_uni + " in reuters: " + str(reuters_freq_dict[tech_uni]))
except KeyError:
    print("Frequency of " + nontech_uni + " in reuters: 0")
try:
    print("Frequency of " + tech_uni + " in twitter samples: " + str(twitter_samples_freq_dict[tech_uni]))
except KeyError:
    print("Frequency of " + tech_uni + " in twitter samples: 0")
try:
    print("Frequency of " + nontech_uni + " in twitter samples: " + str(twitter_samples_freq_dict[nontech_uni]))
except KeyError:
    print("Frequency of " + nontech_uni + " in twitter samples: 0")


