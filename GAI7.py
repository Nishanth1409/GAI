from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
long_text = """
The Indian Penal Code (IPC) is a comprehensive criminal code which covers all aspects of criminal law in India. The IPC was drafted in 1860 and has been amended numerous times over the years. It covers crimes such as theft, murder, defamation, and other offenses. It also outlines the procedures for criminal trials, evidence, and punishment. The IPC serves as the backbone of the criminal justice system in India.
"""
input_length = len(long_text.split())
max_len = min(input_length, 100)
summary = summarizer(long_text, max_length=max_len, min_length=50, do_sample=False)
print(summary[0]['summary_text'])