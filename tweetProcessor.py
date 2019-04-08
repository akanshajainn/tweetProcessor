import re
from filterWords import filterWords


class tweetProcessor(filterWords):
    
    def __init__(self, return_tokens=False, tolower=True):
        self.return_tokens = return_tokens
        self.tolower = tolower

        self.regexp = {"RT": "^RT", 
                       "MT": r"^MT", 
                       "ALNUM": r"(@[a-zA-Z0-9_]+)",
                       "HASHTAG": r"(#[\w\d]+)", 
                       "URL": r"([https://|http://]?[a-zA-Z\d\/]+[\.]+[a-zA-Z\d\/\.]+)",
                       "SPACES": r"\s+"}
        
        self.regexp_dict = dict((key, re.compile(value)) for key, value in self.regexp.items())
        self.stop_words = filterWords.STOP_WORDS
        self.positive = filterWords.POSITIVE
        self.negative = filterWords.NEGATIVE
        self.filterwords =  self.stop_words +  self.positive + self.negative
        
    def process(self, dirty_tweet):
        
        tweet_tokens = list(filter(None, re.split("[., /!?;&:\n]+", str(dirty_tweet))))
        tweet_text = ' '.join(tweet_tokens)
        
        rt = re.findall(self.regexp_dict["RT"], tweet_text)
        hashtag = re.findall(self.regexp_dict["HASHTAG"], tweet_text)
        url = re.findall(self.regexp_dict["URL"], tweet_text)
        username = re.findall(self.regexp_dict["ALNUM"], tweet_text)
        
        filterwords = rt + hashtag + url + username + self.filterwords        
        clean_tweet_tokens = [word for word in tweet_tokens if word not in filterwords]
        if self.tolower:
            clean_tweet_tokens = [word.lower() for word in clean_tweet_tokens if word.lower() not in filterwords]
        clean_tweet_text = ' '.join(clean_tweet_tokens)
        if self.return_tokens:
            return clean_tweet_tokens
        return clean_tweet_text

    def __add_filter_word__(self, word):
        self.filterwords.append(word)