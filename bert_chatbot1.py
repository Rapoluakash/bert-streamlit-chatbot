import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------------
# Load fast MiniLM model
# ------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('paraphrase-MiniLM-L6-v2')

model = load_model()

# ------------------------
# QA Knowledge Base
# ------------------------
qa_pair = {
    "What is your name?": "I am a chatbot powered by MiniLM!",
    "How are you?": "I'm just a bunch of code, but I'm doing great!",
    "What is BERT?": "BERT stands for Bidirectional Encoder Representations from Transformers. It’s a powerful NLP model.",
    "Tell me a joke.": "Why don't programmers like nature? It has too many bugs.",
    "What is data science": "Data Science is the study of analyzing data to find useful information...",
    "What is your use": "A MiniLM-based chatbot uses sentence embeddings to understand and respond...",
    "What is AI": "Artificial Intelligence (AI) is the ability of machines to simulate human intelligence...",
    "What is Microsoft Azure": "Microsoft Azure is a cloud computing platform provided by Microsoft..."
}

# ------------------------
# Get embedding
# ------------------------
def get_embedding(text):
    return model.encode([text])

# ------------------------
# Precompute QA embeddings
# ------------------------
precomputed = {q: get_embedding(q) for q in qa_pair}

# ------------------------
# Chatbot Logic
# ------------------------
def chatbot_response(user_input):
    user_embedding = get_embedding(user_input)
    scores = {
        q: cosine_similarity(user_embedding, precomputed[q])[0][0]
        for q in qa_pair
    }
    best = max(scores, key=scores.get)
    return qa_pair[best] if scores[best] > 0.5 else "I'm not sure how to respond to that."

# ------------------------
# Streamlit UI
# ------------------------
st.title("⚡ Fast MiniLM Chatbot")
st.write("This chatbot uses the lightweight MiniLM model for quick and smart replies!")

st.subheader("Ask me anything:")
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    reply = chatbot_response(user_input)
    st.markdown(f"**Chatbot:** {reply}")
