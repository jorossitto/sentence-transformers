from sklearn.feature_extraction.text import TfidfVectorizer
import re
import string
from nltk.corpus import wordnet

# Enhanced TF-IDF Vectorizer
class EnhancedTfidfVectorizer(TfidfVectorizer):
    def build_preprocessor(self):
        preprocessor = super().build_preprocessor()
        def enhanced_preprocess(doc):
            doc = doc.lower()
            doc = re.sub(f'[{re.escape(string.punctuation)}]', '', doc)
            return preprocessor(doc)
        return enhanced_preprocess

# Synonym-aware analyzer
class SynonymAwareTfidfVectorizer(EnhancedTfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(SynonymAwareTfidfVectorizer, self).build_analyzer()

        def synonym_analyzer(doc):
            synonyms = []
            for word in analyzer(doc):
                synonyms.append(word)
                for syn in wordnet.synsets(word):
                    for lemma in syn.lemmas():
                        synonyms.append(lemma.name())
            return synonyms

        return synonym_analyzer