documents = [
    "Student studies math.",
    "Teacher explains lesson.",
    "Computer runs program.",
    "Model predicts result."
]

processed_docs = [doc.lower().replace(".","") for doc in documents]
print(processed_docs)


vocab = {}
count = 0
for doc in processed_docs:
    for word in doc.split():
        if word not in vocab:
            count = count +1
            vocab[word] = count
print(vocab)


def get_onehot_vector(somestring):
    onehot_encoded = []
    for word in somestring.split():
        temp = [0]*len(vocab)
        if word in vocab:
            temp[vocab[word]-1] = 1 # -1 is to take care of the fact indexing in array starts from 0 and not 1
        onehot_encoded.append(temp)
    return onehot_encoded
print(processed_docs[1])
get_onehot_vector(processed_docs[1])

print(get_onehot_vector(processed_docs[1]))

get_onehot_vector("man and dog are good") 
print(get_onehot_vector("man and dog are good"))



get_onehot_vector("man and man are good") 
print(get_onehot_vector("man and man are good"))



S1 = 'student studies math'
S2 = 'teacher explains lesson'
S3 = 'computer runs program'
S4 = 'model predicts result'

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = [S1.split(), S2.split(), S3.split(), S4.split()]
values = data[0]+data[1]+data[2]+data[3]
print("The data: ",values)

#Label Encoding
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print("Label Encoded:",integer_encoded)

#One-Hot Encoding
onehot_encoder = OneHotEncoder()
onehot_encoded = onehot_encoder.fit_transform(data).toarray()
print("Onehot Encoded Matrix:\n",onehot_encoded)