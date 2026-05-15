from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
documents = [
    "Bạn rất xinh đẹp",
    "Bạn đã thắng giải thưởng lớn",
    "Bạn đã trúng thưởng 20 triệu đồng",
    "Bạn quá tài năng",
    "Tôi quá thất vọng về bạn",
    "Hôm nay tôi buồn quá",
    "Bản thân tôi quá tệ",
    "Tôi ghét bạn"
    
]

doc1=[d.lower().replace(",","") for d in documents]
vocab={}
count=0
for d in doc1:
    for word in d.split():
        if word not in vocab:
            count= count+1
            vocab[word]=count
print(vocab)
doc1= CountVectorizer()
bow_rep = doc1.fit_transform(documents)
for one in range(8):
    print(bow_rep[one].toarray())
    
    

models=["tich_cuc","tich_cuc","tich_cuc","tich_cuc","tieu_cuc","tieu_cuc","tieu_cuc","tieu_cuc"]
model = MultinomialNB()
model.fit(bow_rep,models)
test_doc = [
    "Bạn nữ ấy xinh đẹp",
    "Anh ấy rất đẹp trai",
    "Bà tôi ghét tôi",
    "Bạn Mai đang buồn"
    ]

test_bow_rep = doc1.transform(test_doc)
predicted_labels = model.predict(test_bow_rep)
for doc, label in zip(test_doc, predicted_labels):
    print(f"Văn bản: '{doc}' => Dự đoán: {label}")
    
    
test_models=["tich_cuc","tich_cuc","tieu_cuc","tieu_cuc"]
cm=accuracy_score(test_models,predicted_labels)
print(cm)