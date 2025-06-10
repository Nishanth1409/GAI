
def extract(file):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def search(query, ipc):
    query = query.lower()
    lines = ipc.split("\n")
    results = [line for line in lines if query in line.lower()]
    return results if results else ["No relevant section found."]

def chatbot():
    print("Loading IPC text document...")
    ipc = extract("8prg.txt")  # <-- Make sure your text file is named IPC.txt
    print("IPC document loaded. Type 'exit' to quit.\n")
    
    while True:
        query = input("Ask a question about the IPC: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        results = search(query, ipc)
        print("\n".join(results))
        print("-" * 50)

# Start chatbot
chatbot()
