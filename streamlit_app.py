import streamlit as st
import tempfile
from rag_engine import GenericRAG

st.set_page_config(
    page_title="Student Textbook Chatbot",
    page_icon="📚"
)

st.title("📚 Student Textbook Chatbot")
st.caption("Upload any textbook PDF or TXT file and ask questions")

# -------------------------------
# Session State Initialization
# -------------------------------
if "rag" not in st.session_state:
    st.session_state.rag = GenericRAG()

if "ready" not in st.session_state:
    st.session_state.ready = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_file" not in st.session_state:
    st.session_state.current_file = None

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload a textbook (PDF or TXT)",
    type=["pdf", "txt"]
)

# Build vector store ONLY once per new file
if uploaded_file and uploaded_file.name != st.session_state.current_file:
    with st.spinner("Building knowledge base..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        st.session_state.rag.build_from_file(temp_path)

        st.session_state.current_file = uploaded_file.name
        st.session_state.ready = True
        st.session_state.messages = []

    st.success("Textbook processed and ready!")

# -------------------------------
# Chat UI
# -------------------------------
if st.session_state.ready:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_input := st.chat_input("Ask a question from the book..."):
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.rag.ask(user_input)
                st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
else:
    st.info("Upload a textbook to start chatting.")
