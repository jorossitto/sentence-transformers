from scipy.spatial.distance import cosine
import numpy as np

# Weighted Scoring Function
def weighted_score(tfidf_score, bert_score, tfidf_weight=0.5, bert_weight=0.5):
    return tfidf_weight * tfidf_score + bert_weight * bert_score
def semantic_similarity(embedding1, embedding2):
    """
    Calculate the cosine similarity between two 1-D embeddings.
    """
    # Detach tensors and convert to numpy arrays
    embedding1 = embedding1.detach().numpy()
    embedding2 = embedding2.detach().numpy()

    return 1 - cosine(embedding1, embedding2)

