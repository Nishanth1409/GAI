from langchain_community.llms import Cohere
from langchain.prompts import PromptTemplate
import os

# Set your Cohere API key
COHERE_API_KEY = "uvw9ehIHyTzOwhsYlsRfr6bgQZufcGgp3A0cIYDK"

# Initialize the Cohere LLM with the API key
llm = Cohere(cohere_api_key=COHERE_API_KEY)

# Load the document
file_path = "8prg.txt"

try:
    with open(file_path, "r") as file:
        document_text = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Create the prompt
prompt = PromptTemplate(
    input_variables=["document"],
    template="You are an assistant tasked with analyzing text. Given the following document: {document} Provide a summary in three concise bullet points:"
)

# Format and invoke
formatted_prompt = prompt.format(document=document_text)
response = llm.invoke(formatted_prompt)

# Output
print("Response:")
print(response)
