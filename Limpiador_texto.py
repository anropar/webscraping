import re
import unidecode

def clear_text(text):
    text = unidecode.unidecode(text)
    text = text.upper()
    text = re.sub('[^\w\s]', '', text)
    text = re.sub(' +', ' ', text)
    return text