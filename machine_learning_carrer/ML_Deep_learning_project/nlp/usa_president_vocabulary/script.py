# Required libraries
import os
import gensim
import spacy
from project.machine_learning_carrer.ML_Deep_learning_project.nlp.usa_president_vocabulary.president_helper import read_file, process_speeches, merge_speeches, get_president_sentences, get_presidents_sentences, most_frequent_words

directory_path = './usa_president_pitch'

# List all .txt files in the specified directory
files = sorted([file for file in os.listdir(directory_path) if file.endswith('.txt')])
print(files)

# Reading each speech into a string
speeches = [read_file(file) for file in files]

# Breaking down speeches into sentences then into words
processed_speeches = process_speeches(speeches)

# Merging speeches into a single list of sentences
all_sentences = merge_speeches(processed_speeches)

# Analyzing frequency of words across all speeches
most_freq_words = most_frequent_words(all_sentences)
print(most_freq_words)

# Creating a word embedding model for all inaugural addresses
all_prez_embeddings = gensim.models.Word2Vec(all_sentences, vector_size=96, window=5, min_count=1, workers=2, sg=1)

# Exploring words used in similar contexts to "freedom"
similar_to_freedom = all_prez_embeddings.wv.most_similar("freedom", topn=20)
print(similar_to_freedom)

# Analyzing a single president (Franklin D. Roosevelt)
roosevelt_sentences = get_president_sentences("franklin-d-roosevelt")
roosevelt_most_freq_words = most_frequent_words(roosevelt_sentences)
print(roosevelt_most_freq_words)

# Creating a word embedding model for FDR's speeches
roosevelt_embeddings = gensim.models.Word2Vec(roosevelt_sentences, vector_size=96, window=5, min_count=1, workers=2, sg=1)

#  Exploring words similar to "freedom" in FDR's speeches
roosevelt_similar_to_freedom = roosevelt_embeddings.wv.most_similar("freedom", topn=20)
print(roosevelt_similar_to_freedom)

#  Training a model on a group of selected presidents
selected_presidents = ["washington", "jefferson", "lincoln", "theodore-roosevelt"]
rushmore_prez_sentences = get_presidents_sentences(selected_presidents)
rushmore_most_freq_words = most_frequent_words(rushmore_prez_sentences)
print(rushmore_most_freq_words)

#  Creating word embeddings for the selected group
rushmore_embeddings = gensim.models.Word2Vec(rushmore_prez_sentences, vector_size=96, window=5, min_count=1, workers=2, sg=1)

#  Exploring words similar to "freedom" among the selected presidents
rushmore_similar_to_freedom = rushmore_embeddings.wv.most_similar("freedom", topn=20)
print(rushmore_similar_to_freedom)

#  Creating Word Embeddings for the Mount Rushmore Presidents
rushmore_embeddings = gensim.models.Word2Vec(rushmore_prez_sentences, vector_size=96, window=5, min_count=1, workers=2, sg=1)

#  Exploring "freedom" in Mount Rushmore Presidents' Embeddings
rushmore_similar_to_freedom = rushmore_embeddings.wv.most_similar('freedom', topn=20)
print('Mount Rushmore Presidents Similar to "freedom":', rushmore_similar_to_freedom)

#  Exploring Other Words
# Choose a word from `rushmore_most_freq_words` or any word of interest
# Example: Exploring "democracy"
rushmore_similar_to_democracy = rushmore_embeddings.wv.most_similar('democracy', topn=20)
print('Similar to "democracy" in Mount Rushmore Presidents’ speeches:', rushmore_similar_to_democracy)

