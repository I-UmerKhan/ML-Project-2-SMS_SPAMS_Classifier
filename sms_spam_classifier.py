import streamlit as st
import joblib
import string
import nltk
import pandas as pd

from sklearn.ensemble import VotingClassifier
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()

# Load the saved vectorizer and models
tfidf = joblib.load('vectorizer.pkl')
mnb = joblib.load('mnb.pkl')
etc = joblib.load('etc.pkl')
rf = joblib.load('rf.pkl')

# Load the DataFrame
df_dict = joblib.load('df_dict.pkl')
df = pd.DataFrame(df_dict)

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")
if st.button('Predict'):

    # Preprocess function
    def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)

        y = []  # removing special characters
        for i in text:
            if i.isalnum():
                y.append(i)
        text = y[:]
        y.clear()

        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
            y.append(ps.stem(i))
        return " ".join(y)

    transformed_sms = transform_text(input_sms)

    # Vectorize
    vector_input = tfidf.transform([transformed_sms]).toarray()

    # Train the VotingClassifier
    model = VotingClassifier(estimators=[('rf', rf), ('nb', mnb), ('et', etc)], voting='soft')
    X = tfidf.transform(df['transformed_text']).toarray()
    y = df['target'].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    result = model.predict(vector_input)[0]

    # Display result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
