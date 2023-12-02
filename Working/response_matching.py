from vectorizers import *
from similarity_measures import *
from sklearn.metrics.pairwise import cosine_similarity

# Response Matching Function with Enhanced TF-IDF
def response_matching_complex(llm_response, expected_response, bert_utils):
    vectorizer = SynonymAwareTfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([llm_response, expected_response])
    tfidf_cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    bert_embeddings = bert_utils.encode([llm_response, expected_response])
    bert_cosine_sim = cosine_similarity([bert_embeddings[0]], [bert_embeddings[1]])[0][0]

    return {"TFIDF_Cosine_Similarity": tfidf_cosine_sim, "BERT_Cosine_Similarity": bert_cosine_sim}