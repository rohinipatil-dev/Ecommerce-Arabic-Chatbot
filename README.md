# Ecommerce-Arabic-Chatbot
# 📌 Printerpix Arabic Chatbot  
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)](https://streamlit.io/)  
[![OpenAI](https://img.shields.io/badge/AI-OpenAI%20GPT--4-blue)](https://platform.openai.com/)  
[![Python](https://img.shields.io/badge/Python-3.9%2B-green)](https://www.python.org/)  

An **Arabic language AI chatbot** built with **Streamlit, OpenAI GPT-4, and TF-IDF search** that answers user queries about [Printerpix](https://www.printerpix.co.uk/) products and services.  

---

## ✨ Features  
- 🌐 **Web scraping** – extracts product and service details from the Printerpix website.  
- 🧠 **TF-IDF + cosine similarity** – retrieves the most relevant text snippets.  
- 🤖 **GPT-4 integration** – generates accurate, natural Arabic answers.  
- 💬 **Interactive UI** – Streamlit-based user-friendly chat interface.  
- ⚡ **Lightweight prototype** – no vector DB needed for small-scale use.  

---

## 🛠️ Tech Stack  
- **Python**  
- **Streamlit** – interactive UI  
- **OpenAI SDK (>=1.0.0)** – GPT-4 completions  
- **Requests + BeautifulSoup** – website scraping  
- **scikit-learn** – TF-IDF + cosine similarity  

---

## 📂 Project Flow  
```mermaid
flowchart TD
    A[User Arabic Query] --> B[TF-IDF Vectorizer]
    B --> C[Cosine Similarity Search]
    C --> D[Relevant Website Text]
    D --> E[OpenAI GPT-4 Arabic Assistant]
    E --> F[Streamlit Frontend Response]

⚡ Quick Start
1️⃣ Clone repo
git clone https://github.com/your-username/printerpix-arabic-chatbot.git
cd printerpix-arabic-chatbot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set your OpenAI API key
export OPENAI_API_KEY="your_api_key_here"

4️⃣ Run the app
streamlit run app.py

🚀 Future Improvements

Replace TF-IDF with embeddings + FAISS/Chroma for semantic search.
Support multilingual queries.
Add persistent storage for scraped data.
Deploy app to Streamlit Cloud / Render / Azure.

📜 License
This project is licensed under the MIT License.
