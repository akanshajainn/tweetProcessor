# tweetProcessor

Repository that helps you to clean/tokenise dirty text or tweet without having to install any extra package. It's pure python.

tweetProcessor allows to:

1. Select if you want to tokenise.
2. Select what entity(url, hashtag, username) you want to remove from the tweet.
3. Select if you want to convert text to lowercase or not.
4. Add your own custom filter word.
5. Extract entities(url, hashtag, username) from tweet.

**run_example.py** file has all the examples to test.

**filterWords.py** has class having emoticons and stop words list which you can modify acc to your needs.

Run on terminal:

```
python3 run_example.py
```