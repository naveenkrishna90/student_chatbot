📚 Student Textbook Chatbot (RAG + Vector DB)

A Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload any textbook (PDF or TXT) and ask questions strictly based on the content of that book.

Built using:

LangChain

OpenAI embeddings

FAISS vector database

Streamlit UI


🚀 Features

📄 Upload any textbook (PDF / TXT)

✂️ Automatic text splitting & embedding

🧠 Vector search using FAISS

💬 Chat interface using Streamlit

🎯 Answers strictly grounded in the uploaded textbook

⚡ Vector store created only once per upload (fast queries)

🪵 Detailed logs for ingestion, chunking, and retrieval

🏗️ Architecture (High Level)

Textbook (PDF/TXT)
        ↓
Document Loader
        ↓
Text Splitter
        ↓
Embeddings (OpenAI)
        ↓
FAISS Vector Store
        ↓
Retriever
        ↓
LLM (GPT-4o-mini)
        ↓
Streamlit Chat UI


📁 Project Structure
STUDENT_CHATBOT/
│
├── rag_engine.py          # Core RAG pipeline (ingestion → retrieval)
├── streamlit_app.py       # Streamlit chat interface
├── requirements.txt       # Python dependencies
├── .env                   # OpenAI API key (not committed)
├── README.md              # Project documentation
└── venv/                  # Virtual environment (optional)


⚙️ Prerequisites

Python 3.11

OpenAI API Key

Internet connection

🔐 Environment Setup
1️⃣ Clone the Repository
git clone <your-repo-url>
cd STUDENT_CHATBOT

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set OpenAI API Key

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here


⚠️ Never commit .env to GitHub

▶️ Run the Application
streamlit run streamlit_app.py


Open in browser:

http://localhost:8501


🧪 How to Use

Upload a PDF or TXT textbook

Wait for:

Document loading

Chunking

Vector store creation

Ask questions using the chat box

The chatbot answers only from the uploaded textbook

If the answer is not found:

"I don't know based on the book."

🧠 RAG Pipeline Steps (Implemented)

✔️ Data Ingestion
✔️ Text Splitting
✔️ Embeddings
✔️ Vector Store (FAISS)
✔️ Retrieval + LLM Response

🪵 Logging & Debugging

The app prints detailed logs in the terminal:

Document loading count

Chunk count

Vector store creation time

Query latency

Example:

📄 Loaded 120 pages
✂️ Split into 950 chunks
🔧 Vector store created in 6.4s
❓ Query answered in 1.1s

📦 Dependencies

Key libraries used:

langchain

langchain-community

langchain-openai

faiss-cpu

streamlit

python-dotenv

pypdf

(See requirements.txt for full list)

🔮 Future Enhancements

💾 Persist FAISS index to disk

🔍 Show retrieved source passages

📊 Add confidence score / citations

🌐 Multi-book support

🔄 Streaming responses

🧑‍🏫 Grade-level adaptive explanations

🧑‍💻 Use Cases

School textbook Q&A (Grade 6+)

Teacher assistant

Exam preparation

Curriculum exploration

EdTech product prototype

📜 License

This project is for educational and demo purposes.
Ensure compliance with textbook copyright laws when uploading content.

🙌 Acknowledgements

LangChain

OpenAI

Streamlit

FAISS