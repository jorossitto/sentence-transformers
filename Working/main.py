from sklearn.metrics.pairwise import cosine_similarity
from data_loader import load_json_dataset
#load_json_dataset(file_path)
from text_processing import post_process_response #(response, reference_text, BertUtils)
#post_process_response(response=, reference_text=, BertUtils=)
from bert_utils import BertUtils
#BertUtils.encode(texts=)
#bert_utils.bert_process_text(item['prompt'], item['expectedResponse'])
from response_matching import response_matching_complex, weighted_score

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

# Initialize the BertUtils instance
bert_utils = BertUtils()
# Example usage
json_dataset = load_json_dataset('Data/data.json')
for item in json_dataset:
    # Process text
    llm_response_processed = post_process_response(item['prompt'], bert_utils)
    expected_response_processed = post_process_response(item['expectedResponse'], bert_utils)

    # Calculate semantic similarity
    similarity = bert_utils.bert_process_text(item['prompt'], item['expectedResponse'])
    print(f"Semantic Similarity: {similarity}")

    # Perform response matching and calculate weighted similarity
    scores = response_matching_complex(llm_response_processed, expected_response_processed, bert_utils)
    weighted_similarity = weighted_score(scores['TFIDF_Cosine_Similarity'], scores['BERT_Cosine_Similarity'])

    print(f"Prompt: {item['prompt']}\nExpected Response: {item['expectedResponse']}\nScores: {scores}\nWeighted Score: {weighted_similarity}\n")
