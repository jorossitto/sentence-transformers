import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def post_process_response(response, bert_utils):
    """
    Advanced text manipulation for response normalization and enhancement.
    """
    response = response.strip().lower()

    # Tokenization and other text processing steps
    words = word_tokenize(response)
    pos_tags = nltk.pos_tag(words)
    expanded_response = ' '.join([context_aware_abbreviation_expansion(word, pos) for word, pos in pos_tags])

    # Handling numerical expressions
    expanded_response = re.sub(r'(\d+)\s*-\s*(\d+)', r'\1 to \2', expanded_response)

    # Context-aware synonym replacement
    processed_response = replace_synonyms(expanded_response)

    return processed_response

def replace_synonyms(sentence):
    """
    Replace words in the sentence with their synonyms based on context.
    """
    words = word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)

    new_words = []
    for word, pos in pos_tags:
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        synonyms = set()
        for syn in wordnet.synsets(word, pos=wordnet_pos):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace('_', ' '))
        if synonyms:
            # Choose a synonym that is different from the original word
            new_word = next((syn for syn in synonyms if syn != word), word)
            new_words.append(new_word)
        else:
            new_words.append(word)

    return ' '.join(new_words)

def context_aware_abbreviation_expansion(word, pos):
    """
    Expand abbreviations based on part-of-speech and context.
    """
    abbreviations = {
        "ai": "artificial intelligence",
        "ml": "machine learning",
        "llm": "large language model",
        "nlp": "natural language processing"
    }
    return abbreviations.get(word.lower(), word)

def get_wordnet_pos(treebank_tag):
    """
    Return the WordNet POS tag from the simple POS tag.
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None