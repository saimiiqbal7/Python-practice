import csv

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    new = word
    for punc in punctuation_chars:

       new = (new.replace(punc, ''))
    return (new)


positive_words = []
with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
    
    
def get_pos(sentence):

    num = 0
    for word in sentence.split():
    
        if strip_punctuation(word.lower()) in positive_words:     
            num += 1
    
    return num

negative_words = []
with open("assets/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):

    num = 0
    for word in sentence.split():
    
        if strip_punctuation(word.lower()) in negative_words:     
            num += 1
    
    return num



with open("assets/project_twitter_data.csv", 'r') as f, open("resulting_data.csv", "w") as of:

    data = list(csv.DictReader(f))
   

    retweets = []
    replies = []
    posScores = []
    negScores = []
    netScores = []

    for tweet in data:
        tweetText = (tweet['tweet_text'])
        neg = get_neg(tweetText)
        pos = get_pos(tweetText)

        retweets.append(tweet['retweet_count'])
        replies.append(tweet['reply_count'])
        posScores.append(pos)
        negScores.append(neg)    
        netScores.append(pos-neg)

    writer = csv.writer(of)

    writer.writerow([
        "Number of Retweets",
        "Number of Replies",
        "Positive Score",
        "Negative Score",
        "Net Score"
    ])
    # one output row per tweet
    for rt, rp, ps, ns, net in zip(retweets, replies, posScores, negScores, netScores):
        writer.writerow([rt, rp, ps, ns, net])

# both files auto-closed here
print("✓ resulting_data.csv created")

     
    
    

    




  

    




