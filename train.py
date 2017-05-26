
import os
import sys
import datetime
import numpy as np
import gensim, logging
from gensim.models import Word2Vec
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model

BASE_DIR  = '.'
EMBEDDING = BASE_DIR + '/embeddings/' #'/GoogleNews-Vectors/'
DATA_DIR  = BASE_DIR + '/data/'

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def word2vec_embedding_layer(embeddings_path):
    weights = np.load(open(embeddings_path, 'rb'))
    layer   = Embedding(input_dim=weights.shape[0], output_dim=weights.shape[1], weights=[weights])
    return layer

def load_emb_gensim(embeddings_path):
	model = gensim.models.KeyedVectors.load_word2vec_format(EMBEDDING + 'GoogleNews-vectors-negative300.bin', binary=True)


if __name__ == '__main__':
	#model = gensim.models.KeyedVectors.load_word2vec_format(EMBEDDING + 'GoogleNews-vectors-negative300.bin', binary=True)
	#print("Done " + str(datetime.datetime.now()))
	#weights = model.syn0
	#np.save(open('embeddings.npz', 'wb'), weights)

	input_vec = Input(shape=(300,), dtype='int32', name='input')
	embedding = word2vec_embedding_layer('embeddings.npz') #EMBEDDING + 'GoogleNews-vectors-negative300.bin.gz')
	#embedded = embedding(input_vec)
	
	#model = Word2Vec.load_word2vec_format(EMBEDDING + 'GoogleNews-vectors-negative300.bin.gz', binary=True)	deprecated
	
	
	#model = gensim.models.KeyedVectors.load_word2vec_format(EMBEDDING + 'GoogleNews-vectors-negative300.bin', binary=True)
	print("Done " + str(datetime.datetime.now()))