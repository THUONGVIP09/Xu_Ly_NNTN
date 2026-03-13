from sklearn.feature_extraction.text import CountVectorizer

# Đọc nội dung từ file văn bản
with open("output_bai2.txt", "r", encoding="utf-8") as file:
    doc = file.readlines()

# Xây dựng bộ từ vựng của Kho ngữ liệu
count_vect = CountVectorizer()
bow_rep = count_vect.fit_transform(doc)

# In ra bộ từ vựng
vocab = count_vect.vocabulary_
print("Bộ từ vựng:", vocab)

# Đếm số lần xuất hiện của mỗi từ thủ công
word_count = {}

# Lặp qua từng văn bản và từng từ trong văn bản
for i in range(bow_rep.shape[0]):  # Duyệt qua tất cả các văn bản
    # Lấy các từ đã được mã hóa trong văn bản i
    words_in_doc = bow_rep[i].toarray().flatten()
    
    # Duyệt qua các từ trong từ vựng và đếm số lần xuất hiện
    for word_idx, count in enumerate(words_in_doc):
        if count > 0:  # Nếu từ này xuất hiện trong văn bản
            word = list(vocab.keys())[list(vocab.values()).index(word_idx)]  # Lấy từ từ vocab
            if word in word_count:
                word_count[word] += count  # Tăng số lần xuất hiện của từ
            else:
                word_count[word] = count  # Nếu từ chưa có, khởi tạo số lần xuất hiện

# Sắp xếp từ điển theo số lần xuất hiện giảm dần
sorted_vocab = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

# In 10 từ xuất hiện nhiều nhất
print("10 từ xuất hiện nhiều nhất:")
for word, count in sorted_vocab:
    print(f"{word}: {count}")
# Lấy chỉ số của 10 từ xuất hiện nhiều nhất trong vocab
top_words = [word for word, _ in sorted_vocab]
top_words_index = [vocab[word] for word in top_words]

# Biểu diễn Vector One-hot cho 10 từ xuất hiện nhiều nhất
print("Vector One-hot cho 10 từ xuất hiện nhiều nhất:")
for word in top_words:
    index = vocab[word]  # Lấy chỉ số của từ trong vocab
    one_hot_vector = [0] * len(vocab)  # Tạo vector toàn 0
    one_hot_vector[index] = 1  # Đánh dấu vị trí của từ bằng 1
    print(f"One-hot vector cho từ '{word}': {one_hot_vector}")

# Biểu diễn toàn bộ văn bản bằng Bag-of-Words (BoW) cho câu đầu tiên
print("Bag-of-Words cho câu đầu tiên:", bow_rep[0].toarray())