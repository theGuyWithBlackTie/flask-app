from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
from server import app
from server import config
import math

stopwords = set(stopwords.words('english'))
wordlemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')

def preprocess(text):
    text = str(text)
    text = text.lower()

    cleantext = re.sub('<.*?>', '', text)
    rem_num   = re.sub('[0-9]+', '', cleantext)
    tokens    = tokenizer.tokenize(rem_num)

    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords]
    lemma_words    = [wordlemmatizer.lemmatize(w) for w in filtered_words]

    return lemma_words

def get_tf_idf(text):
    tokens = preprocess(text)

    cache = app.config[config.CACHE].cached_tf_dict

    if len(cache) <=0:
        return None
        
    result_json = {}

    # calculate idf first
    idf_dict = {}
    for each_token in tokens:
        count = 0
        for key in cache:
            if each_token in cache.get(key).keys():
                count += 1
        if count == 0:
            count = 1
        idf_dict[each_token] = math.log(len(cache)/count)

    # 
    for key in cache:
        tf_dict = cache.get(key)
        tf_idf = 0
        for each_token in tokens:
            tf = tf_dict.get(each_token, 0)/len(tf_dict)
            
            tf_idf += tf * idf_dict.get(each_token)
        result_json[key+".txt"] = tf_idf
    
    return result_json

