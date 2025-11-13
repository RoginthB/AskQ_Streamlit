import os
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
#from sklearn.metrics.pairwise import cosine_similarity
#from langchain_community.document_loaders import pyPDFLoader
from dotenv import load_dotenv
load_dotenv()
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("google_api_key"))
# result  = llm.invoke("Sing a balled of langchain.")
# print(result.content)
#print(f" dir : { os.getcwd()}")

# model = init_chat_model("google_genai:gemini-2.5-flash-lite", api_key=os.getenv("google_api_key"))
# response = model.invoke("why do birds sing?")
# print(response.text)


"""#example for Text Splitter"""
def text_splitter(doucument):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = splitter.split_text(document)
    return chunks

def create_vector(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model ="models/gemini-embedding-001",api_key=os.getenv("google_api_key"))
    vector =embeddings.embed_query(chunks)
    return vector


if __name__ == "__main__":
    print(len(create_vector("hello world")))


# from pypdf import PdfReader
# from langchain.text_splitter import CharacterTextSplitter  
# from langchain.vectorstores import FAISS
# from langchain.embeddings import GoogleGenAIEmbeddings
# from langchain.chat_models import ChatGoogleGenAI
# from langchain.chains import RetrievalQA
# import streamlit as st
# import os
# from dotenv import load_dotenv
# load_dotenv()

# def extract_text_from_pdf(file_path):
#     reader = PdfReader(file_path)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() + "\n"
#     return text


# def chunk_text(text):
#     splitter = CharacterTextSplitter(seprator="\n", chunk_size=1000, chunk_overlap=200)
#     return splitter.split_text(text)


# def create_vector_db(chunks):
#     embeddings = GoogleGenAIEmbeddings(api_key=os.getenv("google_api_key"))
#     vector_db = FAISS.from_texts(chunks, embedding=embeddings)
#     return vector_db


# def create_qa_chain(vector_db):
#     llm = ChatGoogleGenAI(model="gemini-flash-sb", api_key=os.getenv("google_api_key"))
#     chain= RetrievalQA.from_chain_type(llm=llm,retriever=vector_db.as_retriever())
#     return chain




# if __name__ == "__main__":
#     st.title("AskQ: PDF Question Answering App")
#     uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
#     question = st.text_input("Ask a question about the PDF: ")

#     if uploaded_file and question:
#     # with open("temp.pdf", "wb") as f:
#     #     f.write(uploaded_file.getbuffer())
    
#         text = extract_text_from_pdf(uploaded_file)
#         chunks = chunk_text(text)
#         vector_db = create_vector_db(chunks)
#         qa_chain = create_qa_chain(vector_db)

#         answer = qa_chain.run(question)
#         st.write("Answer:", answer)