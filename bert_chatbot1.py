import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import base64

# ------------------------
# Background Image (optional)
# ------------------------
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ✅ Use relative path for GitHub/Streamlit Cloud
set_background("assets/background.jpg")  # Optional

# ------------------------
# Load model
# ------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ------------------------
# Knowledge base (QA pairs)
# ------------------------
qa_pair = {
    "What is your name?": "I am a chatbot powered by MiniLM!",
    "How are you?": "I'm just a bunch of code, but I'm doing great!",
    "What is BERT?": "BERT stands for Bidirectional Encoder Representations from Transformers.",
    "Tell me a joke.": "Why don't programmers like nature? It has too many bugs.",
    "What is data science": "Data Science involves extracting knowledge from data using statistics and machine learning.",
    "What is your use": "I help answer your questions using sentence similarity and pre-trained models.",
    "What is AI": "AI is the simulation of human intelligence in machines.",
    "What is Microsoft Azure": "Azure is Microsoft’s cloud computing platform."
}

# ------------------------
# Precompute embeddings
# ------------------------
@st.cache_resource
def get_precomputed_embeddings():
    return {q: model.encode(q, convert_to_numpy=True) for q in qa_pair}

predefined_embeddings = get_precomputed_embeddings()

# ------------------------
# Chatbot logic
# ------------------------
def chatbot_response(user_input):
    user_embedding = model.encode(user_input, convert_to_numpy=True)

    similarities = {
        q: cosine_similarity([user_embedding], [predefined_embeddings[q]])[0][0]
        for q in qa_pair
    }

    best_match = max(similarities, key=similarities.get)
    if similarities[best_match] > 0.5:
        return qa_pair[best_match]
    else:
        return "I'm not sure how to respond to that."

# Streamlit UI

st.title("🤖 MiniLM Chatbot (Fast BERT)")
st.write("Ask a question about AI, data, or tech!")

user_input = st.text_input("You:", placeholder="Type your question here...")

if user_input:
    response = chatbot_response(user_input)
    st.markdown(f"**Chatbot:** {response}")

st.markdown("---")
st.caption("Optimized with sentence-transformers for fast response 🚀")
