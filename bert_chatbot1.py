import streamlit as st
from transformers import BertModel, BertTokenizer
import torch
from sklearn.metrics.pairwise import cosine_similarity

# ------------------------
# Load BERT model/tokenizer
# ------------------------
@st.cache_resource
def load_bert_model():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    return tokenizer, model

tokenizer, model = load_bert_model()

# ------------------------
# QA pairs (your chatbot's knowledge base)
# ------------------------
qa_pair = {
    "What is your name?": "I am a chatbot powered by BERT!",
    "How are you?": "I'm just a bunch of code, but I'm doing great!",
    "What is BERT?": "BERT stands for Bidirectional Encoder Representations from Transformers. It’s a powerful NLP model.",
    "Tell me a joke.": "Why don't programmers like nature? It has too many bugs.",
    "What is data science": "Data Science is the study of analyzing data to find useful information...",
    "What is your use": "A BERT-based chatbot uses the BERT model to understand and respond...",
    "What is AI": "Artificial Intelligence (AI) is the ability of machines to simulate human intelligence...",
    "What is Microsoft Azure": "Microsoft Azure is a cloud computing platform provided by Microsoft..."
}

# ------------------------
# Get BERT embedding
# ------------------------
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

# ------------------------
# Precompute embeddings for questions
# ------------------------
predefined_embeddings = {q: get_embedding(q) for q in qa_pair}

# ------------------------
# Chatbot response logic
# ------------------------
def chatbot_response(user_input):
    user_embedding = get_embedding(user_input)

    similarities = {
        question: cosine_similarity(user_embedding, predefined_embeddings[question])[0][0]
        for question in qa_pair
    }

    best_match = max(similarities, key=similarities.get)
    if similarities[best_match] > 0.5:
        return qa_pair[best_match]
    else:
        return "I'm not sure how to respond to that."

# ------------------------
# Streamlit UI
# ------------------------
st.title("🤖 BERT Chatbot")
st.write("This is a BERT-powered chatbot built with Streamlit. Ask a question to get started.")

st.subheader("Ask me anything:")

user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    response = chatbot_response(user_input)
    st.markdown(f"**Chatbot:** {response}")

st.markdown("---")
