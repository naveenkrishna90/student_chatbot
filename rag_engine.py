import os
import time
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class GenericRAG:
    def __init__(
        self,
        model_name="gpt-4o-mini",
        embedding_model="text-embedding-3-small",
        chunk_size=800,
        chunk_overlap=150
    ):
        print("🔹 Initializing RAG engine")

        self.embeddings = OpenAIEmbeddings(
            model=embedding_model,
            openai_api_key=OPENAI_API_KEY
        )

        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0,
            openai_api_key=OPENAI_API_KEY
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        self.vectorstore = None
        self.qa_chain = None

    def build_from_file(self, file_path: str):
        print(f"\n📄 Loading document: {file_path}")
        start_time = time.time()

        ext = Path(file_path).suffix.lower()
        loader = PyPDFLoader(file_path) if ext == ".pdf" else TextLoader(file_path)

        documents = loader.load()
        print(f"✅ Loaded {len(documents)} raw pages")

        chunks = self.text_splitter.split_documents(documents)
        print(f"✂️ Split into {len(chunks)} chunks")

        print("🔧 Creating vector store (FAISS)...")
        vs_start = time.time()

        self.vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        print(f"✅ Vector store created in {time.time() - vs_start:.2f}s")

        prompt = PromptTemplate(
            template="""
You are a helpful teacher.

Answer the question using ONLY the textbook content.
If the answer is not present, say:
"I don't know based on the book."

Context:
{context}

Question:
{question}

Answer:
""",
            input_variables=["context", "question"]
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 4}),
            chain_type="stuff",
            return_source_documents=False,
            chain_type_kwargs={"prompt": prompt}
        )

        print(f"🎉 RAG pipeline ready in {time.time() - start_time:.2f}s")

    def ask(self, question: str) -> str:
        if not self.qa_chain:
            raise ValueError("Vector store not initialized")

        print(f"\n❓ Query received: {question}")
        start = time.time()

        result = self.qa_chain.invoke({"query": question})

        print(f"⏱️ Query answered in {time.time() - start:.2f}s")
        return result["result"]
