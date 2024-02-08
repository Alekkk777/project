# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import pandas as pd
import numpy as np
from articles import articles  # Make sure to have articles.py with a list named articles
from preprocessing import preprocess_text  # Make sure preprocessing.py has preprocess_text function

# Print one article to read its content
print("Original Article:\n", articles[0])

# Preprocess articles
processed_articles = [preprocess_text(article) for article in articles]
print("Processed Article:\n", processed_articles[0])

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and Transform with CountVectorizer
counts = vectorizer.fit_transform(processed_articles)

# Initialize TfidfTransformer with `norm=None`
transformer = TfidfTransformer(norm=None)

# Fit and Transform with TfidfTransformer
tfidf_scores_transformed = transformer.fit_transform(counts)

# Initialize TfidfVectorizer with `norm=None`
vectorizer_tfidf = TfidfVectorizer(norm=None)

# Fit and Transform with TfidfVectorizer
tfidf_scores = vectorizer_tfidf.fit_transform(processed_articles)

#  Check if tf-idf Scores Are Equal
if np.allclose(tfidf_scores_transformed.todense(), tfidf_scores.todense()):
    print("Are the tf-idf scores the same?: YES")
else:
    print("Are the tf-idf scores the same?: No, something is wrong :(")

#  Preparing DataFrame for easier manipulation
try:
    feature_names = vectorizer_tfidf.get_feature_names_out()
except AttributeError:  # For older versions of scikit-learn
    feature_names = vectorizer_tfidf.get_feature_names()

article_index = [f"Article {i+1}" for i in range(len(articles))]
df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=article_index)

#Identify document topics by highest-scoring tf-idf term
for i in range(1, 11):  # Assuming there are 10 articles
    highest_term = df_tf_idf[f'Article {i}'].idxmax()
    print(f"Article {i} highest TF-IDF term: {highest_term}")
