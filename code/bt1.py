import nltk

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize


 #lọc từ 

text=" This is a sample sentence showing stopword removal."

stop_words=set(stopwords.words('english'))
tokens=word_tokenize(text.lower())

filtered_tokens=[word for word in tokens if word in stop_words]


print("Filtered:",filtered_tokens)
# tìm từ đồng nghĩa
syn=wordnet.synsets("sample")
output=set()
for s in syn:
   
    for l in s.lemmas():
        output.add(l.name())
print("Synonyms of 'sample':",output)

# tách chữ
from nltk import word_tokenize, sent_tokenize
text="Hello there, how are you? Weather is great, and Python is awesome. The sky is blue."
print(word_tokenize(text))
#tach câu
print(sent_tokenize(text))

#Rút gọn từ gốc

from nltk.stem import PorterStemmer 
porter=PorterStemmer()
print( porter.stem("playing"))
print( porter.stem("played"))
print( porter.stem("plays"))
# Chuuan hóa từ
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print( lemmatizer.lemmatize("running","v"))
print( lemmatizer.lemmatize("runs","v"))
print( lemmatizer.lemmatize("run","v"))

#POS Tagging
from nltk import pos_tag
from nltk import word_tokenize
text="They refuse to permit us to obtain the refuse permit"
tokens=word_tokenize(text)
tagged=nltk.pos_tag(tokens)
print(tagged)

