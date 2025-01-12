# Text Document Search and Ranking with BM25 and Inverted Index

_This project made for data-structure class_

A Python program that preprocesses text documents (stemming, stopword removal),
builds an inverted index, and ranks documents based on a user-provided search phrase using the BM25 ranking algorithm.

We use **NLTK library** for tokenize and stemming

Also we use NLTK Gutenberg Corpus that includes 18 books
https://www.nltk.org/book/ch02.html

For ***Ranking System*** we use **Rank Bm25** library
https://pypi.org/project/rank-bm25/ 

The ***inverted index is a dictionary*** that have the above form:
Key: the word
Value: A list with tuples (DocID, The count of word)
e.g {dad [(0,3)(1,4)]
     hello[(1,5)(2,1)]}

Finally we print the results in a list (DocId, RankScore)

Also we write the Inverted index At a Result.txt file

The runtime of program for 18 books usually takes close to 23 seconds.
