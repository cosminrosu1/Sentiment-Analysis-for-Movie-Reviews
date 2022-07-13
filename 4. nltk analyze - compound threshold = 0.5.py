from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

threshold = 0.5

pos_count = 0
total_count = 0
pos_correct = 0

with open("positive.txt", "r", encoding="utf-8") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= threshold or vs['compound'] <= -threshold:
            if vs['compound'] > 0:
                pos_correct += 1
            pos_count += 1
        total_count += 1


neg_count = 0
total_count = 0
neg_correct = 0

with open("negative.txt", "r", encoding="utf-8") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= threshold or vs['compound'] <= -threshold:
            if vs['compound'] <= 0:
                neg_correct += 1
            neg_count += 1
        total_count += 1

print("Positive accuracy = {}% via {} samples out of {} samples.".format(pos_correct/pos_count*100.0, pos_count, total_count))
print("Negative accuracy = {}% via {} samples out of {} samples.".format(neg_correct/neg_count*100.0, neg_count, total_count))