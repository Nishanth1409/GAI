import re

# Function to load the IPC document
def load_ipc_text(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()
		
# Function to search for the relevant section based on the question
def search_ipc_section(question, ipc_text):
    match = re.search(r"section (\d+)", question, re.IGNORECASE)
    if not match:
        return "Please ask about a specific section number (e.g., 'What is Section 302?')"

    section_number = match.group(1)
    sections = ipc_text.split("Section ")
    
    for sec in sections:
        if sec.startswith(f"{section_number}."):
            return "Section " + sec.strip()
    
    return f"Sorry, Section {section_number} not found in the IPC."

def ipc_chatbot():
	# Load the IPC document
	ipc_text = load_ipc_text('ipc.txt')
	print("Indian Penal Code Chatbot :")
	print("You can ask about any section of the IPC. Type 'exit' to quit.")
		
	while True:
		# Take user input
		question = input("You: ")
		if question.lower() == 'exit':
			break
			
		# Get the answer from the IPC text
		answer = search_ipc_section(question, ipc_text)
			
		# Display the response
		print("Bot:", answer)

if __name__ == "__main__":

	ipc_chatbot()
