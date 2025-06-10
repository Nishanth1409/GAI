from langchain_community.llms import Cohere
from langchain.prompts import PromptTemplate
import os
COHERE_API_KEY = "ahS1Pdd1C6Kq5lm8cOPIBWrN0zc0wEg9O0AwRjbS"
llm = Cohere(cohere_api_key=COHERE_API_KEY)
file_path = "8prg.txt"
try:
    with open(file_path, "r") as file:
        document_text = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()
prompt = PromptTemplate(
    input_variables=["document"],
    template="You are an assistant tasked with analyzing text. Given the following document: {document} Provide a summary in three concise bullet points:"
)
formatted_prompt = prompt.format(document=document_text)
response = llm.invoke(formatted_prompt)
print("Response:")
print(response)
