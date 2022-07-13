from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from collections import Counter

analyzer = SentimentIntensityAnalyzer()

correct_pos = []
incorrect_pos = []
unidentified_pos = []

with open("positive_formatted.txt", "r", encoding="utf-8") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['neg'] < 0.1:
            if vs['pos']-vs['neg'] > 0:
                correct_pos.append(line)
            else:
                incorrect_pos.append(line)
        else:
            unidentified_pos.append(line)

all_words_pos = []
for i in range(0, len(correct_pos)):
    for word in correct_pos[i].split():
        k = analyzer.polarity_scores(word)
        if k['pos'] > 0:
            all_words_pos.append(word)

common_words_pos = []
common_words_count_pos = []

for word, count in Counter(all_words_pos).most_common(10):
    common_words_pos.append(word)
    common_words_count_pos.append(count)

fig = plt.figure(figsize=(10, 5))

plt.bar(common_words_pos, common_words_count_pos, color='green', width=0.5)
plt.xlabel("Cuvinte")
plt.ylabel("Nr. de apariții")
plt.title("Cele mai întâlnite cuvinte pozitive")
plt.show()

correct_neg = []
incorrect_neg = []
unidentified_neg = []

with open("negative_formatted.txt", "r", encoding="utf-8") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['pos'] < 0.1:
            if vs['pos']-vs['neg'] <= 0:
                correct_neg.append(line)
            else:
                incorrect_neg.append(line)
        else:
            unidentified_neg.append(line)

all_words_neg = []
for i in range(0, len(correct_neg)):
    for word in correct_neg[i].split():
        k = analyzer.polarity_scores(word)
        if k['neg'] > 0:
            all_words_neg.append(word)

common_words_neg = []
common_words_count_neg = []

for word, count in Counter(all_words_neg).most_common(10):
    common_words_neg.append(word)
    common_words_count_neg.append(count)

fig = plt.figure(figsize=(10, 5))

plt.bar(common_words_neg, common_words_count_neg, color='red', width=0.5)
plt.xlabel("Cuvinte")
plt.ylabel("Nr. de apariții")
plt.title("Cele mai întâlnite cuvinte negative")
plt.show()