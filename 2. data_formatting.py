import nltk
import string
import enchant

reviews = []

with open("positive.txt", "r", encoding="utf-8") as f:
    for line in f.read().split('\n'):
        reviews.append(line)

stop_words = set(nltk.corpus.stopwords.words('english'))
exclude_words = {"no", "wasn't", "shouldn't", "won't", "couldn't", "very", "aren't", "most", "more", "don't", "too",
                 "wouldn't", "weren't", "isn't", "doesn't", "hadn't", "haven't", "not", "such", "hasn't", "mustn't",
                 "didn't", "mightn't", "needn't"}
new_stop_words = list(stop_words.difference(exclude_words))

stop_words_capitalized = []
for i in range(0, len(new_stop_words)):
    stop_words_capitalized.append(new_stop_words[i].title())
    new_stop_words.append(stop_words_capitalized[i])

for i in range(0, len(reviews)):
    for word in reviews[i].split():
        if word in new_stop_words:
            reviews[i] = reviews[i].replace(word + ' ', '')

punctuation = string.punctuation
punctuation = punctuation.replace("'", '')
punctuation = punctuation.replace('!', '')
punctuation = punctuation.replace(':', '')
punctuation = punctuation.replace('(', '')
punctuation = punctuation.replace(')', '')

for i in range(0, len(reviews)):
    for word in reviews[i]:
        reviews[i] = reviews[i].translate(str.maketrans('', '', punctuation))

dictionary = enchant.Dict("en_US")

for i in range(0, len(reviews)):
    for word in reviews[i].split():
        if dictionary.check(word) is False:
            if '!' not in word and ':' not in word:
                reviews[i] = reviews[i].replace(word, '')
    reviews[i] = reviews[i].strip()

with open("positive_formatted.txt", 'w', encoding="utf-8") as output:
    for row_review in reviews:
        output.write(str(row_review) + '\n')