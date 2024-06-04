from flask import Flask, render_template, request, redirect
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os

# Set up OpenAI API key
OPENAI_API_KEY = "sk-proj-******************"
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

app = Flask(__name__)

vectorstore = None
conversation_chain = None
chat_history = []

PREDEFINED_PDF_PATHS = [r"C:\Users\moner\Downloads\application\New folder\docs\UAE_website_text.pdf"]

def get_pdf_text(pdf_paths):
    text = ""
    for pdf_path in pdf_paths:
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(model="gpt-4")
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/process', methods=['POST'])
def process_documents():
    global vectorstore, conversation_chain
    raw_text = get_pdf_text(PREDEFINED_PDF_PATHS)
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    conversation_chain = get_conversation_chain(vectorstore)
    return redirect('/chat')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global vectorstore, conversation_chain, chat_history

    if request.method == 'POST':
        user_question = request.form['user_question']
        modified_question = "Please answer the question based solely on the document content: " + user_question
        response = conversation_chain({'question': modified_question})
        chat_history = response['chat_history']

    return render_template('chat1.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
