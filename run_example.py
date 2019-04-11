from tweetProcessor import tweetProcessor

'''
Purposefully used dirty texts to show versatility of the code
'''

if __name__ == '__main__':

	tp = tweetProcessor(tokenise = False)  # create tweetProcessor object. 

	# Example 1

	dirty_text1 = "RT @gerald: It's bout that time were I feel like beening a HARD WORKING WOMAN .....and a stripper hoe by night don't judge me &#workhard #playhard"

	print("*" * 5, "Example 1", "*"*5)
	print("dirty_text1 before processing: ", dirty_text1)
	print("dirty_text1 after processing: ", tp.process(dirty_text1), "\n")

	# Example 2

	dirty_text2 = 'RT @JBoxJohnson: She idiot&#128109; He stupid&#128108;She a hoe&#128129;She pregnant&#128124;He sell drugs&#127811;They smoke weed&#127811;=( They drunk&#127866;who Cares? LEAVE PEOPLE ALONE!!!! Its &#8230;'

	print("*" * 5, "Example 2", "*"*5)
	print("dirty_text2 before processing: ", dirty_text2)
	print("dirty_text2 after processing: ", tp.process(dirty_text2), "\n")

	# Example 3 : If you want to add your own word which you want to remove from the sentence.
	#			  Let's remove 'hoe' from dirty_text2 which was not removed before.

	tp.__add_filter_word__('hoe') 	# command which adds custom filter word to be removed.

	print("*" * 5, "Example 3", "*"*5)
	print("dirty_text2 after processing and removing custom word: ", dirty_text2)		
	print("dirty_text2 after processing and removing custom word: ", tp.process(dirty_text2), "\n")		

	# Example 4 : To extract entities like hashtags, usernames from the text.

	dirty_text3 = 'RT @goodvibes: When the girl with the aux cord playin some #trashshit... http://t.co/o5eZd8FSq9'

	print("*" * 5, "Example 4", "*"*5)
	print("dirty_text3 before processing: ", dirty_text3)
	print("dirty_text3 after processing: ", tp.process(dirty_text3))
	print("Entities dirty_text3 contains: ", tp.extract(dirty_text3), "\n")

	# Example 5 : To tokenise the text/tweet and removing only stop words.
	
	tokeniser = tweetProcessor(tokenise=True, remove_rt = False, filter_hashtag=False, filter_url=False, filter_usr=False, tolower=False)
	print("*" * 5, "Example 5", "*"*5)
	print("Tokenising dirty_text1 : ",tokeniser.process(dirty_text1), "\n")

	# Example 6 : To tokenise the text/tweet and removing stop words and lowercasing each word.

	tokeniser1 = tweetProcessor(tokenise=True, remove_rt = False, filter_hashtag=False, filter_url=False, filter_usr=False, tolower=True)
	print("*" * 5, "Example 6", "*"*5)
	print("Tokenising dirty_text1 (with lowercase): ",tokeniser1.process(dirty_text1), "\n")

	# Example 7 : To tokenise the text/tweet and keeping hashtags.

	tokeniser2 = tweetProcessor(tokenise=True, remove_rt = True, filter_hashtag=False, filter_url=True, filter_usr=True, tolower=True)
	print("*" * 5, "Example 7", "*"*5)
	print("Tokenising dirty_text1 : ",tokeniser2.process(dirty_text1), "\n")

	# Example 8 : To tokenise the text/tweet and remove all unwanted words.
	
	tokeniser3 = tweetProcessor(tokenise=True, remove_rt = True, filter_hashtag=True, filter_url=True, filter_usr=True, tolower=True)
	print("*" * 5, "Example 8", "*"*5)
	print("Tokenising dirty_text1 : ",tokeniser3.process(dirty_text1))
