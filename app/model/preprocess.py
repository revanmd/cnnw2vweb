import pandas as pd
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

class Preprocess:
	def __init__(self):
		self.__DATASET = None
		#self.__KORPUS_FENOMENA = None
		#self.__KORPUS_HAPUS = None
		self.__STEMMER = None
		self.__STOPWORD = None

	"""

	SETTER GETTER 

	"""

	def read_dataset(self, dataframe):
		self.__DATASET = dataframe

	#def read_korpus_fenomena(self,dataframe):
	#	self.__KORPUS_FENOMENA = dataframe

	#def read_korpus_hapus(self,dataframe):
	#	self.__KORPUS_HAPUS = dataframe

	"""

	SETUP BEFORE USED

	"""

	def setup_stemmer(self):
		factori = StemmerFactory()
		self.__STEMMER = factori.create_stemmer()

	def setup_stopword(self):
		#if self.__KORPUS_HAPUS is not None:
			#deleted_word = self.__KORPUS_HAPUS['deleted_word'].tolist()
		all_stopword = StopWordRemoverFactory().get_stop_words()# + deleted_word
		dictionary = ArrayDictionary(all_stopword)
		stopword = StopWordRemover(dictionary)

		self.__STOPWORD = stopword 

	"""

	OUR PREPROCESSING METHOD

	"""

	# clean text including (symbol, emoticon, punctuation)
	def clean_text(self,text):
		print('run clean text')
		return re.sub(r"[^a-zA-Z0-9]+", ' ', text)

	def clean_digit(self,text):
		print('run clean digit')
		return re.sub(r'[^a-z ]*([.0-9])*\d', '', text)

	def clean_unknown_word(self,text):
		print('run clean unkown word')
		temp = []
		for item in set(text.split()):
			if(len(item)>=3):
				temp.append(item)
		output = ' '.join([str(elem) for elem in temp]) 
		return output

	def clean_repeated_character(self,text):
		print('run clean repeated character')
		return re.sub(r'(.)\1{2,}', r'\1', text)

	def tokenize(self,text):
		print('run tokenize')
		return nltk.word_tokenize(text)

	def stopword_removal(self,text):
		print('run stopword removal')
		return self.__STOPWORD.remove(text)

	def stemming(self,text):
		print('run stemming')
		return self.__STEMMER.stem(text)


	"""
	
	MAIN PREPARATION

	"""
	# normalisasi - stopword removal - stemming
	def prepare_dataset_1(self):
		print('running -> prepare dataset 1')
		self.__DATASET['review'] = self.__DATASET['review'].astype(str)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_text)
		self.__DATASET['review'] = self.__DATASET['review'].str.lower()
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_digit)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_repeated_character)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.stopword_removal)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.stemming)

	# normalisasi - stopword removal
	def prepare_dataset_2(self):
		print('running -> prepare dataset 2')
		self.__DATASET['review'] = self.__DATASET['review'].astype(str)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_text)
		self.__DATASET['review'] = self.__DATASET['review'].str.lower()
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_digit)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_repeated_character)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.stopword_removal)

	# normalisasi 
	def prepare_dataset_3(self):
		print('running -> prepare dataset 3')
		self.__DATASET['review'] = self.__DATASET['review'].astype(str)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_text)
		self.__DATASET['review'] = self.__DATASET['review'].str.lower()
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_digit)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_repeated_character)

	# normalisasi - stemming
	def prepare_dataset_4(self):
		print('running -> prepare dataset 4')
		self.__DATASET['review'] = self.__DATASET['review'].astype(str)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_text)
		self.__DATASET['review'] = self.__DATASET['review'].str.lower()
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_digit)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.clean_repeated_character)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.stemming)


	# stemming - stopword removal
	def prepare_dataset_5(self):
		print('running -> prepare dataset 5')
		self.__DATASET['review'] = self.__DATASET['review'].astype(str)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.stopword_removal)
		self.__DATASET['review'] = self.__DATASET['review'].apply(self.stemming)

	def to_csv(self,filename):
		self.__DATASET.to_csv(f'{filename}.csv',index=False)

	def to_list(self):
		return self.__DATASET['review']
