from model import preprocess

prep = preprocess.Preprocess()
read = prep.setup_stopword()
read = prep.setup_stemmer()