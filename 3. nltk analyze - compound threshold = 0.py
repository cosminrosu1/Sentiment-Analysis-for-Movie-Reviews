from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

pos_count = 0
pos_correct = 0

with open("positive.txt", "r", encoding="utf-8") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] > 0:
            pos_correct += 1
        pos_count += 1

neg_count = 0
neg_correct = 0

with open("negative.txt", "r", encoding="utf-8") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] <= 0:
            neg_correct += 1
        neg_count += 1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))