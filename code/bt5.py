#câu 1a
#code mẫu trong slide

doc=[
    "Student studies math.",
    "Teacher explains lesson.",
    "Computer runs program.",
    "Model predicts result."
]
doc1=[d.lower().replace(",","") for d in doc]
vocab={}
count=0
for d in doc1:
    for word in d.split():
        if word not in vocab:
            count= count+1
            vocab[word]=count
print(vocab)

def onehot(somestring):
    onehot=[]
    for word in somestring.split():
        temp=[0]*len(vocab)
        if word in vocab:
            temp[vocab[word]-1]=1
        onehot.append(temp)
    return onehot
for one in range(4):
    print(onehot(doc1[one]))
#dùng thư viện
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


data = [word for d in doc1 for word in d.split()]
print("Data:", data)


label = LabelEncoder()
integer = label.fit_transform(data)
print("Integer labels:", integer)

data2 = [[word] for d in doc1 for word in d.split()]

onehot2 = OneHotEncoder()  
onehot3 = onehot2.fit_transform(data2).toarray()
print("One-hot encoding:", onehot3)
        
#câu 1b

from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
bow_rep=count_vect.fit_transform(doc)
print("our vocab:",count_vect.vocabulary_)
print("bow 1:",bow_rep[0].toarray())
temp=count_vect.transform(["student and student are math"])
print(temp.toarray())




