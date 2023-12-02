from transformers import AutoModel, AutoTokenizer
from sentence_transformers import SentenceTransformer
from similarity_measures import *

class BertUtils:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/graphcodebert-base")
        self.model = AutoModel.from_pretrained("microsoft/graphcodebert-base")
        self.sentence_model = SentenceTransformer('bert-base-nli-mean-tokens')

    def bert_process_text(self, text, reference_text):
        """
        Process the text through BERT and compare its semantic similarity to a reference text.
        """
        inputs = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
        ref_inputs = self.tokenizer(reference_text, return_tensors='pt', max_length=512, truncation=True)

        outputs = self.model(**inputs)
        ref_outputs = self.model(**ref_inputs)

        text_embedding = outputs.last_hidden_state[:, 0, :].squeeze()
        ref_embedding = ref_outputs.last_hidden_state[:, 0, :].squeeze()

        # Debugging: Print the shape of the embeddings
        print(f"Text Embedding Shape: {text_embedding.shape}")
        print(f"Ref Embedding Shape: {ref_embedding.shape}")
        return semantic_similarity(text_embedding, ref_embedding)

    def process_single_text(self, text):
        """
        Process a single text input using BERT.
        """
        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True)

        # Process through BERT
        outputs = self.model(**inputs)

        # Extract embeddings or other relevant features
        # For example, using the [CLS] token embedding
        embedding = outputs.last_hidden_state[:, 0, :].squeeze()

        # Return the processed text or embedding
        return embedding  # or some other processing based on your needs

    def encode(self, texts):
        return self.sentence_model.encode(texts)