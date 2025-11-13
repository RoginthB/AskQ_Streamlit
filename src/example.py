import os
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
#from langchain_community.document_loaders import pyPDFLoader
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("google_api_key"))
result  = llm.invoke("Sing a balled of langchain.")
print(result.content)

#Multimodal invocation with gemini-pro-vision

message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe the image."},
        {
            "type": "image_url",
            "image_url": {
                "url": "https://example.com/path/to/your/image.jpg"
            }
        }
    ]
)