from flask import Blueprint, render_template,request
from markupsafe import escape
from .model import model as models
from .model import dataset
from .model import preprocess
from keras.preprocessing.text import Tokenizer
import tensorflow as tf
import keras
import pandas as pd
import pickle

routes = Blueprint('routes',__name__)

model = keras.models.load_model('./app/dataset_3.h5')
tokenizer = None
with open('./app/tokenizer.pkl', 'rb') as file:
    # Call load method to deserialze
    tokenizer = pickle.load(file)

def validator(ind):
	if len(ind) > 2:
		return False

	ind = int(ind) - 1
	if ind >= 0 and ind <= 9:
		return True

	return False

def preprocessing_text(ulasan,id_prep):
	df = pd.DataFrame({'review':[ulasan]})
	prep = preprocess.Preprocess()
	prep.read_dataset(df)
	prep.setup_stemmer()
	prep.setup_stopword()

	if id_prep == 1:
		prep.prepare_dataset_1()
	elif id_prep == 2:
		prep.prepare_dataset_2()
	elif id_prep == 3:
		prep.prepare_dataset_3()
	elif id_prep == 4:
		prep.prepare_dataset_4()
	elif id_prep == 5:
		prep.prepare_dataset_5()


	return prep.to_list()

def prediction(ulasan,id_prep):

	sequence = preprocessing_text(ulasan,id_prep)
	sequences_token = tokenizer.texts_to_sequences(sequence)
	sequences_pad = tf.keras.preprocessing.sequence.pad_sequences(sequences_token,maxlen=150)
	predictions = model.predict(sequences_pad)

	return predictions

@routes.route('/')
def route_home():
	return render_template('index.html')

@routes.route('/doc/recent')
def doc():
	return render_template('/admin/layout.html')

@routes.route('/doc/model/<id>')
def doc_model(id):
	if(validator(id)):
		id = int(id)
		next_url = None
		prev_url = None

		if(id == 1):
			next_url = "/doc/model/"+str(2)
			prev_url = "/doc/model/"+str(10)
		elif(id == 10):
			next_url = "/doc/model/"+str(1)
			prev_url = "/doc/model/"+str(9)
		else:
			next_url = "/doc/model/"+str(id+1)
			prev_url = "/doc/model/"+str(id-1)

		id = id - 1
		d = models.get_model(id)

		return render_template('/admin/model.html',d = d, next_url = next_url, prev_url = prev_url)
	else:
		return render_template('404.html')

@routes.route('/doc/dataset/<id>')
def doc_dataset(id):
	if(validator(id)):
		id = int(id)
		next_url = None
		prev_url = None

		if(id == 1):
			next_url = "/doc/dataset/"+str(2)
			prev_url = "/doc/dataset/"+str(10)
		elif(id == 10):
			next_url = "/doc/dataset/"+str(1)
			prev_url = "/doc/dataset/"+str(9)
		else:
			next_url = "/doc/dataset/"+str(id+1)
			prev_url = "/doc/dataset/"+str(id-1)

		id = id - 1
		d = dataset.get_dataset(id)

		return render_template('/admin/dataset.html',d = d, next_url = next_url, prev_url = prev_url)
	else:
		return render_template('404.html')

@routes.route('/doc/hasil')
def doc_classification():
	return render_template('/admin/hasil.html')

@routes.route('/doc/demo')
def form_demo():
	return render_template('/admin/demo.html', res = "")


@routes.route('/doc/submit', methods=['POST'])
def form_submit():
	ulasan = request.form['ulasan']
	id_prep = int(request.form['id_prep'])

	sentimen = prediction(ulasan,id_prep)
	label = ""

	if sentimen > 0.5:
		label = "Positif"
	else:
		label = "Negatif"

	if sentimen == 0.49040422:
		label = "Tidak dikenali"
	return render_template('/admin/demo.html', res = ulasan, label=label, probability=sentimen)

	return ulasan