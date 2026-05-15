import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences   
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, LSTM


# Dữ liệu mẫu
texts=[
     "cổ phiếu ngân hàng tăng mạnh",
    "thị trường chứng khoán giảm điểm",
    "doanh thu quý này tăng cao",
    "lợi nhuận doanh nghiệp vượt kỳ vọng",
    "đội tuyển bóng đá thắng trận",
    "ca sĩ ra mắt album mới",
    "du lịch hè rất nhộn nhịp",
    "bộ phim mới đạt doanh thu phòng vé cao",
]

#1.Kinh tế/Kinh doanh, 0. Không phải
labels=[1,1,1,1,0,0,0,0]
#Train-test split
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42)
#Tokenization
max_words = 1000
max_len = 10

tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

X_train_pad = pad_sequences(X_train_seq, maxlen=max_len, padding='post')
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len, padding='post')
#Xây dựng mô hình CNN
model=Sequential(
    [
        Embedding(input_dim=max_words, output_dim=32, input_length=max_len),
        LSTM(64),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
        
        
    ]
)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Train
model.fit(X_train_pad, np.array(y_train), epochs=10, batch_size=2, verbose=1)
#Đánh giá
loss, accuracy = model.evaluate(X_test_pad, np.array(y_test), verbose=0)
print(f"Độ chính xác: {accuracy:.4f}")

#Dự đoán
new_texts = [
    "doanh thu quý này giảm mạnh",
    "đội tuyển bóng đá thua trận"
]
new_seq = tokenizer.texts_to_sequences(new_texts)
new_pad = pad_sequences(new_seq, maxlen=max_len, padding='post')
predictions = model.predict(new_pad)
for text, pred in zip(new_texts, predictions):
    label = "Kinh tế/Kinh doanh" if pred[0] > 0.5 else "Không phải"
    print(f"Văn bản: '{text}' => Dự đoán: {label} (Xác suất: {pred[0]:.4f})")