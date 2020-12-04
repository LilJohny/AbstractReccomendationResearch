from gensim.models import KeyedVectors
import pandas as pd

WORD_VECTORS = KeyedVectors.load("../data/vectors_new_v2.kv", mmap='r')
NETFLIX_ID_TO_MOVIE_DICT = pd.read_pickle("../data/netflix_id_to_movie_dict.pkl") #
MOVIE_TO_NETFLIX_ID_DICT = {name: film_id for film_id, name in NETFLIX_ID_TO_MOVIE_DICT.items()}
AVAILABLE_MOVIES_TITLES = set(MOVIE_TO_NETFLIX_ID_DICT.keys())

