
import os
import sys
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model

BASE_DIR  = ''
EMBEDDING = BASE_DIR + '/GoogleNews-Vectors/'
DATA_DIR  = BASE_DIR + '/data/'
