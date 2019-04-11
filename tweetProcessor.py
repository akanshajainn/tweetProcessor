import re
from .filterWords import filterWords

'''
Preprocessing Tool that removes stopwords, positive emoticons, negative emoticons, @usernames, #hashtags, urls, rt from a text/tweet.
It also has a function to extract hashtags, username mentioned, urls in the text/tweet.
You can choose to return clean text or tokenised clean text.
'''

class tweetProcessor(filterWords):
    
    def __init__(self, tokenise=False, tolower=True, filter_hashtag=True, filter_url=True, filter_usr=True, remove_rt=True):
        self.tokenise = tokenise
        self.tolower = tolower
        self.filter_hashtag = filter_hashtag
        self.filter_url = filter_url
        self.filter_usr = filter_usr
        self.remove_rt = remove_rt
        self.regexp = {"RT": "^RT", 
                       "MT": r"^MT", 
                       "USR": r"(@[a-zA-Z0-9_]+)",
                       "HASHTAG": r"(#[\w\d]+)", 
                       "URL": r"http\S+",
                       "SPACES": r"\s+"}
        
        self.regexp_dict = dict((key, re.compile(value)) for key, value in self.regexp.items())
        self.stop_words = filterWords.STOP_WORDS
        self.positive = filterWords.POSITIVE
        self.negative = filterWords.NEGATIVE
        self.filterwords =  self.stop_words +  self.positive + self.negative
        
    def __add_filter_word__(self, word):
        self.filterwords.append(word)

    def process(self, dirty_tweet):
        
        if self.remove_rt:
            dirty_tweet = re.sub(self.regexp['RT']," ",dirty_tweet)

        if self.filter_url:
            dirty_tweet = re.sub(self.regexp['URL']," ",dirty_tweet)

        if self.filter_usr:
            dirty_tweet = re.sub(self.regexp['USR']," ",dirty_tweet)

        if self.filter_hashtag:
            dirty_tweet = re.sub(self.regexp['HASHTAG']," ",dirty_tweet)

        tweet_tokens = list(filter(None, re.split("[., /!?;&:\"\n]+", str(dirty_tweet))))
        tweet_text = ' '.join(tweet_tokens)

        clean_tweet_tokens = [word for word in tweet_tokens if word not in self.filterwords]  

        if self.tolower:
            clean_tweet_tokens = [word.lower() for word in clean_tweet_tokens if word.lower() not in self.filterwords]

        clean_tweet_text = ' '.join(clean_tweet_tokens)

        if self.tokenise:
            return clean_tweet_tokens
        return clean_tweet_text

    def extract(self, dirty_tweet):
        
        rt = re.findall(self.regexp_dict["RT"], dirty_tweet)
        hashtag = re.findall(self.regexp_dict["HASHTAG"], dirty_tweet)
        url = re.findall(self.regexp_dict["URL"], dirty_tweet)
        username = re.findall(self.regexp_dict["USR"], dirty_tweet)

        if len(rt):
            return {'RT':True, 'HASHTAGS':hashtag, 'URLS':url, 'USR_MENTIONED':username}
        else:            
            return {'RT':False, 'HASHTAGS':hashtag, 'URLS':url, 'USR_MENTIONED':username}
