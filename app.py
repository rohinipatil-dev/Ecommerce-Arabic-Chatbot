import os
import streamlit as st
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

client = OpenAI()

@st.cache_data
def scrape_website_data():
    url = "https://al-sadhan.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract visible text from the website
    texts = []
    for p in soup.find_all(["p", "h1", "h2", "h3", "h4", "li"]):
        text = p.get_text(strip=True)
        if text:
            texts.append(text)
    return texts

@st.cache_data
def prepare_vectorizer(texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    return vectorizer, tfidf_matrix

def get_most_relevant_text(query, texts, vectorizer, tfidf_matrix):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, tfidf_matrix)
    idx = np.argmax(similarity)
    return texts[idx]

def generate_response(user_query, context):
    messages = [
        {"role": "system", "content": "You are a helpful Arabic-speaking assistant."},
        {"role": "user", "content": f"استند على المعلومات التالية للرد بدقة على السؤال: {context}\nسؤال: {user_query}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content

def main():
    st.title("Arabic AI Assistant")
    st.write("مرحباً! أنا مساعدك الذكي، اسألني أي شيء ترغب بمعرفته.")

    texts = scrape_website_data()
    vectorizer, tfidf_matrix = prepare_vectorizer(texts)

    user_query = st.text_input("اكتب سؤالك هنا:")
    if st.button("إرسال"):
        if user_query.strip():
            relevant_text = get_most_relevant_text(user_query, texts, vectorizer, tfidf_matrix)
            answer = generate_response(user_query, relevant_text)
            st.markdown(f"**الجواب:** {answer}")

if __name__ == "__main__":
    main()

