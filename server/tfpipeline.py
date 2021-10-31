import re
import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

class TF:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        self.wordlemmatizer = WordNetLemmatizer()
        self.tokenizer = RegexpTokenizer(r'\w+')

    def get_TF(self, file):
        with open(file, 'r') as handle:
            file_data = handle.read()

        tokens = self.preprocess(file_data)
        
        tf_dict= {}
        for each_token in tokens:
            tf_dict[each_token] = tf_dict.get(each_token, 0.0) + 1.0

        return tf_dict

    def preprocess(self, text):
        text = str(text)
        text = text.lower()

        cleantext = re.sub('<.*?>', '', text)
        rem_num   = re.sub('[0-9]+', '', cleantext)
        tokens    = self.tokenizer.tokenize(rem_num)

        filtered_words = [w for w in tokens if len(w) > 2 if not w in self.stopwords]
        lemma_words    = [self.wordlemmatizer.lemmatize(w) for w in filtered_words]

        return lemma_words


