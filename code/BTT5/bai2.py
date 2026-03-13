from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
documents = [
    "Nhấn vào link này để nhận quà miễn phí ngay hôm nay",
    "Bạn đã thắng giải thưởng lớn, hãy nhấn vào đây để nhận quà",
    "Bạn đã trúng thưởng 20 triệu đồng, bấm vào để nhận tiền",
    "Đây là cơ hội duy nhất để bạn nhận được phần thưởng lớn, hãy nhấn vào đây",
    "Bạn đã trúng thưởng 50 triệu đồng, hãy nhấn vào đây để nhận tiền",
    "Em gửi anh tài liệu họp để anh xem trước chiều nay",
    "Anh có thể giúp em sửa bài tập về nhà được không?",
    "Em cần giúp đỡ với bài tập toán, anh có thể giúp em không?",
    "Anh có thể giúp em chuẩn bị bài thuyết trình cho lớp học không?",
    "Shop xác nhận đơn hàng của bạn sẽ được giao vào ngày mai"
]

doc1= CountVectorizer()
bow_rep = doc1.fit_transform(documents)

models=["Spam","Spam","Spam","Spam","Spam","Ham","Ham","Ham","Ham","Ham"]
model = MultinomialNB()
model.fit(bow_rep,models)
test_doc = [
    "Nhấn vào đây để nhận quà miễn phí ngay hôm nay",
    "Anh có thể giúp em sửa bài tập về nhà được không?",
    "Nhập thông tin ngân hàng để nhận hoàn tiền từ chương trình khuyến mãi",
    "Mai nhóm mình họp lúc 8 giờ để chốt phần thuyết trình"
    ]
test_bow_rep = doc1.transform(test_doc)
predicted_labels = model.predict(test_bow_rep)
for doc, label in zip(test_doc, predicted_labels):
    print(f"Văn bản: '{doc}' => Dự đoán: {label}")
    