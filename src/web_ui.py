import streamlit as st
import random
import time
from openai import OpenAI
from dotenv import load_dotenv

class Ui:
    def __init__(self):
        pass

    def response_generator(self):
        response = random.choice(
            ["hello there! how can I assist you today?", "hi, human! Is there anything I can help you with"]
        )
        for word in response.split():
            yield word + " "
            time.sleep(0.2)

    def home_page(self):

        st.title("AskQ")
        if "messages" not in st.session_state:
            st.session_state.messages =[]
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        if prompt :=st.chat_input("what is up?"):
            st.session_state.message.append({"role":"user","content":prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response =st.write_stream(self.response_generator())
            st.session_state.messages.append({"role":"assistant", "content":response})


class Chat_with_OpenAI:
    
    def __init__(self):
        pass
    def start(self):
        load_dotenv()
        st.title("askQ")

        client =OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"]="gemini-2.5-flash"
        if "messages" not in st.session_state:
            st.session_state.messages =[]

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt :=st.chat_input("what is up?"):
            st.session_state.messages.append({"role":"user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

        with st.chat_message("assistant"):
            stream =client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content":m["content"]} 
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role":"assistant", "content":response})
