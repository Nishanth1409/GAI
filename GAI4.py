from gensim.downloader import load 
import torch 
from transformers import pipeline 
model = load("glove-wiki-gigaword-50") 
torch.manual_seed(42)
def enrich(prompt): 
    enriched_prompt = prompt
    words = prompt.split()
    for word in words: 
        try:
            similar_words = model.most_similar(word, topn=3) 
            print(f"Similar words for '{word}':", similar_words)
            synonyms = [w for w, _ in similar_words]
            enriched_prompt += " " + " ".join(synonyms)
        except KeyError:
            print(f"'{word}' not found in GloVe model.")
            continue
    return enriched_prompt
original_prompt = "lung cancer"
enriched_prompt = enrich(original_prompt)
print("\nOriginal Prompt:", original_prompt)
print("Enriched Prompt:", enriched_prompt)
generator = pipeline("text-generation", model="gpt2")
response_original = generator(original_prompt, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
print("\nGenerated Text (Original Prompt):\n", response_original[0]["generated_text"])
response_enriched = generator(enriched_prompt, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
print("\nGenerated Text (Enriched Prompt):\n", response_enriched[0]["generated_text"])
