import tensorflow as tf
import tensorflow_hub as hub
import sys
import pickle
import nltk
import spacy


path ='./'
SPECIAL_TAGS = '@.' # remplace les caractères spéciaux
encoder_url = "https://tfhub.dev/google/universal-sentence-encoder/4"

def ListToString(liste):
    listSaveWords = []
    liste2 = liste.copy()
    for word in liste:
        if word.find('+')!=-1 or word.find('#')!=-1:
            saveWord = word
            liste2[liste.index(saveWord)] = SPECIAL_TAGS # special tags
            listSaveWords.append(saveWord)
            
    phrase = ' '.join(liste2)
    return (phrase,listSaveWords)

def textProcessing(text):
    text = text.lower()
    tokenizerText = nltk.RegexpTokenizer(r'([A-Za-z0-9+#]+)')
    tokenText = tokenizerText.tokenize(text)
    with open(path + 'StopWord.pickle','rb') as f:
        sw = pickle.load(f)
    tokens_WSW = [word for word in tokenText if word not in sw and not word.isnumeric()]
    # lemmatization
    nlp = spacy.load("en_core_web_sm")
    text, listSaveWords = ListToString(tokens_WSW)
    doc = nlp(text)
    liste = []
    k=0
    for token in doc:
    	#print(token)
        if str(token.lemma_) == SPECIAL_TAGS:
        	token = listSaveWords[k]
        	k=+1
        	liste.append(token)
        else:
        	liste.append(token.lemma_)
    TokenLemma = liste
    # end lemmatization
    sentence = [' '.join(TokenLemma).strip()]
    print(sentence,file=sys.stderr)
    encoderModel = hub.load(encoder_url)
    res = encoderModel(sentence)
    print(res,file=sys.stderr)
    return res

def numericToReducedTags(integerList,labels):
	reducedTags=[]
	for i,j in zip(integerList,labels):
		if i == 1:
			reducedTags.append(j)
	return reducedTags
	
def ReducedTagsToStackTags(RTags, dicoP):
	Tags = []
	for i in RTags:
		Tags.append(dicoP[i])
	return Tags
