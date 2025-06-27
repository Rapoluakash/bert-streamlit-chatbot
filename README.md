#🤖 BERT Streamlit Chatbot

A simple and interactive chatbot built with BERT (Bidirectional Encoder Representations from Transformers) and Streamlit. This chatbot can answer basic predefined questions using semantic similarity powered by BERT embeddings.

screenshot

#🚀 Features

🤖 BERT-based question-answer matching
💬 Chat-like interface with Streamlit
🎨 Customizable background image
⚡ Fast response using cosine similarity
🧠 Pre-trained bert-base-uncased model from HuggingFace
#📁 Project Structure

bert-streamlit-chatbot/ │ ├── app.py # Main chatbot app ├── requirements.txt # Python dependencies ├── README.md # Project overview and usage ├── .gitignore # Ignored files and folders ├── assets/ │ └── background.jpg # Optional: background image └── utils/ └── bert_utils.py # (Optional) reusable BERT utility functions

yaml Copy Edit

#🔧 Installation

1Clone the repo:

git clone https://github.com/your-username/bert-streamlit-chatbot.git
cd bert-streamlit-chatbot
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
🖼️ Custom Background (Optional)
Replace assets/background.jpg with your own image and update the path in the set_background() function inside app.py.

✨ Example Questions
What is your name?

What is BERT?

Tell me a joke.

What is data science?

How are you?

📦 Dependencies
transformers

torch

streamlit

scikit-learn

numpy

Install with:

bash
Copy
Edit
pip install -r requirements.txt
📜 License
MIT License. Feel free to use and modify.

👨‍💻 Author
Rapolu Akash
📧 rapoluakash3@gmail.com

⭐ Show some love!
If you find this useful, give it a ⭐ on GitHub!

yaml
Copy
Edit

---

Let me know if you want:
- A logo/banner for GitHub
- To split `app.py` into modules (`utils/bert_utils.py`)
- A sample `screenshot.png` mockup

Want me to create a zip or push-ready repo folder for download?
