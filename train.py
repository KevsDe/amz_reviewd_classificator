import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, confusion_matrix
from sklearn.svm import SVC
import src.text_analysis as ta


df_class = pd.read_csv('output/df_class.csv')

tfidf = TfidfVectorizer(tokenizer=ta.nltk_tokenizer)

X = tfidf.fit_transform(df_class['text'].values.astype('U'))

print("Training the model")

model = SVC()
model.fit(X, df_class['quality'].values)

with open ('amz_reviews_model.bin', 'wb') as f:
    pickle.dump((tfidf,model), f)

print("Model training completed")