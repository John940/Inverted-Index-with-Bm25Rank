#This project made for data-structure class
import time
import os
start = time.time()
from nltk.corpus import gutenberg
from string import punctuation
from rank_bm25 import BM25Okapi
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english') # The list with the stopwords
for i in punctuation:
    stop_words.append(i)    # We append at the stopwords list, the punctuation (expecting better results)

books_collection = nltk.corpus.gutenberg.fileids()   # This is the books at .txt form (this collection have 18 books)

the_inverted_index = dict()  # Key = The Words, value = a List with tuples (DocID, Count)

docs = []    # The list that we are store the books
for i in range(17): # index range 1-17 (because we have 18 books)
    docs.append(gutenberg.raw(books_collection[i]))  # Insert at the list, the content of every book ,as String


#.....Otherwise you can read your ownn .txt files.....
#mypath = r"C:\Users\user\Example\Exam"
#books_collection = os.listdir(mypath)
#for i in range(len(books_collection)):
#    docs.append(open(mypath + '\\' + books_collection[i]).read())

docs = [wordpunct_tokenize(doc) for doc in docs]  # tokenize every book

docs_with_stopping_stemming =[]  #new list that we store the results after stopping and stemming

ps = PorterStemmer()
for i in range (len(docs)):
    docs_with_stopping_stemming.append([])
    for k in range(len(docs[i])):
        if docs[i][k].lower() not in stop_words:   # for every word in the book check if it is a stopword
            docs_with_stopping_stemming[i].append(ps.stem(docs[i][k].lower()))    # Then apply stemming, and store it in the new list



for i in range(len(docs_with_stopping_stemming)): # for every book
    count_term = dict()   # create a temporary dictionary
    for term in docs_with_stopping_stemming[i]:
        if term not in count_term:  # If word not in temporary dictionary
            count_term[term] = 1
        else:                      
            count_term[term] += 1
    for term in count_term:  #for every word of the book in temporary dictionary
        if term not in the_inverted_index:   # if not in final index..
            the_inverted_index[term] = []
        the_inverted_index[term].append((i, count_term[term]))    #Insert the results of every word at the final inverted index as tuple (DocId, Count)

        
user_phrase = "Best places for programmers all around the world" #  Searching Phrase
user_phrase_token = wordpunct_tokenize(user_phrase)    # tokenize
user_phrase_token = [word for word in user_phrase_token if not word in stop_words]  # check for stopwords
user_phrase_token = [ps.stem(word).lower() for word in user_phrase_token]   # stemming

#Using Bm250 library to take rank results
bm25 = BM25Okapi(docs_with_stopping_stemming) 
doc_scores = bm25.get_scores(user_phrase_token)    # a list with rank score for every book

#Writting the Results at a .txt file
try:
    f = open("results.txt", "w")
except:
    print("Error at opening the file..")

for key,value in the_inverted_index.items():
    try:
        f.write(str(key) + str(value) +"\n")
    except UnicodeEncodeError:
        print("Can't encode the word: " + str(key) + str(value))

f.close()

final_scores = []
for i in range(len(doc_scores)):
    final_scores.append((i, doc_scores[i]))


final_scores.sort(reverse= True,key= lambda x : x[1])
print(final_scores) 


end = time.time()
print(f"Runtime of the program is {end - start}")



