# SMS_SPAMS_Classifier

I recently completed an SMS spam classifier project, which involved several steps to ensure its accuracy and user-friendliness. Here’s a detailed breakdown of what I did:

1. **Data Cleaning**: I began by removing unwanted columns that contained many null values and eliminated duplicate entries to ensure the dataset was clean and reliable.

2. **Feature Engineering**: Using the nltk library, I created new features, including the number of words, the number of characters, and the number of sentences in each message. This helped in gaining better insights during exploratory data analysis (EDA).

3. **Text Preprocessing**: I removed stopwords and special characters from the messages to standardize the text. Additionally, I applied stemming to reduce words to their base form, which further improved the quality of the data.

4. **Visualization**: To better understand the distribution and commonalities in normal and spam messages, I utilized word clouds. This visualization technique provided a clear insight into the most frequently occurring words in each category.

5. **Model Training**: I trained multiple machine learning models to determine the best-performing one. After evaluating their performance, I found that a voting classifier yielded the best results.

6. **Model Deployment**: I serialized the best-performing model and the base models using pickle. Additionally, I saved the TF-IDF vectorizer to ensure consistent text vectorization during deployment.

7. **User Interface Development**: I loaded the models and the vectorizer into PyCharm and used Streamlit to develop a user-friendly layout. This interface was deployed on localhost, making it easy for users to interact with the SMS spam classifier.

By following these steps, I was able to create an effective and user-friendly SMS spam classification system.


**Testing on spam messages**

![image](https://github.com/I-UmerKhan/SMS_SPAMS_Classifier/assets/103349712/b901deea-4ce3-4ac9-a2b3-46d975e2543e)
![image](https://github.com/I-UmerKhan/SMS_SPAMS_Classifier/assets/103349712/e069736d-12c8-45ed-9c84-2aa47c937010)
![image](https://github.com/I-UmerKhan/SMS_SPAMS_Classifier/assets/103349712/61aacdcb-8318-4b90-a96b-db300a3634c9)

**Testing on messages that arent spam**
![image](https://github.com/I-UmerKhan/SMS_SPAMS_Classifier/assets/103349712/169819bb-db51-49cf-97b9-361cb9f31773)
![image](https://github.com/I-UmerKhan/SMS_SPAMS_Classifier/assets/103349712/8ef70f6c-1027-48a7-a2b5-64cd07020763)
![image](https://github.com/I-UmerKhan/SMS_SPAMS_Classifier/assets/103349712/488c1afe-8e57-4b95-9523-b9cbf42b9645)







