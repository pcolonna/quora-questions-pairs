
import os
import sys
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model

BASE_DIR  = '.'
EMBEDDING = BASE_DIR + '/embeddings/' #'/GoogleNews-Vectors/'
DATA_DIR  = BASE_DIR + '/data/'

def word2vec_embedding_layer(embeddings_path):
    weights = np.load(open(embeddings_path, 'rb'))
    layer   = Embedding(input_dim=weights.shape[0], output_dim=weights.shape[1], weights=[weights])
    return layer

if __name__ == '__main__':
	input_vec = Input(shape=(300,), dtype='int32', name='input')
	embedding = word2vec_embedding_layer(EMBEDDING + 'GoogleNews-vectors-negative300.bin.gz')
	embedded = embedding(input_vec)