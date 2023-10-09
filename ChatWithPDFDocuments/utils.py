from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

from dotenv import load_dotenv
from pathlib import Path

base_path=Path(__file__.rsplit('\\', 1)[0])
load_dotenv(base_path.parent / '.env')

def get_prompt_template():
    prompt_template = """You are a helpful AI assistant. Kindly, answer the question based on the passed context.
    If you could not find any answer based on  the passed context, do not generate any random infomrmation.
    Just return "I couldn't find an answer based on the retrived context!"

    Context:
    {context}

    Question: {question}
    Answer:"""

    return PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

def create_vector_db(chunks, embedding):
    print('Created and saved to disk!')
    db = FAISS.from_texts(chunks, embedding)
    save_index(db)
    return db

def save_index(db):
    db.save_local(base_path / "faiss_index")

def load_index(embedding):
    return FAISS.load_local(str(base_path / "faiss_index"), embedding)

def delete_index():
    if (base_path / 'faiss_index').is_dir():
        for f in (base_path / 'faiss_index').iterdir():
            f.unlink()
        (base_path / 'faiss_index').rmdir()

def pdf_to_text(pdfs):
    full_text = ""
    for pdf in pdfs:
        reader = PdfReader(pdf)

        for page in reader.pages:
            full_text += page.extract_text()

    return full_text

def split_text(text):
    splitter = CharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=25,
        separator='\n',
        length_function=len
    )
    return splitter.split_text(text)

def get_embedding_model():
    return OpenAIEmbeddings()

def get_llm():
    return ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)

def get_memory():
    return ConversationBufferMemory(memory_key='chat_history', return_messages=True)

def get_chain(llm, retriever, memory, prompt):
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt},
        chain_type="stuff"
    )