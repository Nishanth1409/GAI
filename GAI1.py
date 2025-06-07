# Import the KeyedVectors class from gensim.models which is used to load and work with word vectors
from gensim.models import KeyedVectors  

def explore_word_relationships(model_path):  
    """
    This function demonstrates the famous 'king - man + woman = queen' word vector analogy
    using pre-trained word embeddings.
    
    Args:
        model_path (str): Path to the pre-trained word2vec model file
    """
    try:  
        # Load the pre-trained word vectors model
        print("Loading the model...") 
        word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True)  
        print("Model loaded successfully!")

        # Define the words we want to use for the analogy
        words = ['king', 'man', 'woman']   
        
        # Check if all required words exist in the model
        for word in words:  
            if word not in word_vectors:  
                print(f"Warning: '{word}' not found in the model.")  
                return  

        # Perform the vector arithmetic: king - man + woman
        # This should result in a vector close to 'queen'
        result_vector = word_vectors['king'] - word_vectors['man'] + word_vectors['woman']

        # Find the 5 most similar words to our resulting vector
        similar_words = word_vectors.similar_by_vector(result_vector, topn=5)

        # Print the results with their similarity scores
        print("Similar words found:")  
        for word, score in similar_words:  
            print(f"{word}: {score}")  
    except Exception as e:  
        print(f"Error: {e}")

# Path to the pre-trained Google News word vectors model
# Note: You need to download this file separately and update the path accordingly
model_path = 'GoogleNews-vectors-negative300.bin'  

# Call the function to perform the word relationship exploration
explore_word_relationships(model_path)
