from tweetProcessor import tweetProcessor

if __name__ == '__main__':

	tp = tweetProcessor(return_tokens = False)  # create tweetProcessor object

	# Example 1

	dirty_text1 = 'RT @iadorewomen_: A couple &#128107; is "A couple" &#128076; Not "A couple &amp; one" &#128107;&#128694; Not "A couple &amp; some" &#128107;&#128582;&#128581;&#128129; Not "A couple &amp; plenty" &#128107; &#128131;&#128131;&#128131;&#128131;&#128131; No hoes No &#8230;'
	print("Example 1 before processing: ", dirty_text1)
	print("Example 1 after processing: ", tp.process(dirty_text1), "\n")

	# Example 2

	dirty_text2 = 'RT @JBoxJohnson: She idiot&#128109; He stupid&#128108;She a hoe&#128129;She pregnant&#128124;He sell drugs&#127811;They smoke weed&#127811;=( They drunk&#127866;who Cares?!!!!!!!!!! LEAVE PEOPLE ALONE Its &#8230;'
	print("Example 2 before processing: ", dirty_text2)
	print("Example 2 after processing: ", tp.process(dirty_text2), "\n")

	# Example 3 : If you wangt to add yopur own word which you want to remove from the sentence.
	#			  Let's remove 'hoe' from dirty_text2 which was not removed before.

	tp.__add_filter_word__('hoe') 	# command which adds custom filter word to be removed.

	print("Example 2 after processing and removing custom word: ", dirty_text2)		
	print("Example 2 after processing and removing custom word: ", tp.process(dirty_text2))		