import requests 
from bs4 import BeautifulSoup 
import operator 
import pandas as pd
from collections import Counter 

def start(url): 
	wordlist = [] 
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code, 'html.parser')
	for each_text in soup.findAll():
		content = each_text.text
		words = content.lower().split() 
		for each_word in words:
			wordlist.append(each_word) 
		return (clean_wordlist(wordlist)) 

# Function removes any unwanted symbols 
def clean_wordlist(wordlist): 
	
	clean_list =[]
	for word in wordlist:
		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		for i in range (0, len(symbols)):
			word = word.replace(symbols[i], '')
		if len(word) > 0:
			clean_list.append(word) 
	return (clean_commonword(clean_list))

# Function removes most common words in list
def clean_commonword(clean_list):
    clean_commonlist=[]
    common_words_df = pd.read_csv('list.txt', names=['words'])
    common_wordslist = common_words_df['words'].values.tolist()
    clean_commonlist = [word for word in clean_list if word not in common_wordslist]
    return (create_dictionary(clean_commonlist))

# Creates a dictionary conatining each word's count and top_20 ocuuring words 
def create_dictionary(clean_commonlist): 
	word_count = {} 
	for word in clean_commonlist: 
		if word in word_count: 
			word_count[word] += 1
		else: 
			word_count[word] = 1
	c = Counter(word_count)  
	top = c.most_common(15) 
	return (top) 