from gensim.models import KeyedVectors  
def explore_word_relationships(model_path):  
    try:  
        print("Loading the model...") 
        word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True)  
        print("Model loaded successfully!")
        words = ['king', 'man', 'woman']   
        for word in words:  
            if word not in word_vectors:  
                print(f"Warning: '{word}' not found in the model.")  
                return  
        result_vector = word_vectors['king'] - word_vectors['man'] + word_vectors['woman']
        similar_words = word_vectors.similar_by_vector(result_vector, topn=5)
        print("Similar words found:")  
        for word, score in similar_words:  
            print(f"{word}: {score}")  
    except Exception as e:  
        print(f"Error: {e}")
model_path = 'GoogleNews-vectors-negative300.bin'  # Modify as per your path   
explore_word_relationships(model_path)
