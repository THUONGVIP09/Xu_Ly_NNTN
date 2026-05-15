
import json
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

def load_json_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def describe_dataset(data):
    total_samples = len(data)

    # Đếm số mẫu theo label
    labels = [item.get("label") for item in data if "label" in item]
    label_count = Counter(labels)

    class_0 = label_count.get(0, 0)
    class_1 = label_count.get(1, 0)

    # Tính tỷ lệ
    if class_1 != 0:
        ratio_0_1 = class_0 / class_1
    else:
        ratio_0_1 = None

    if class_0 != 0:
        ratio_1_0 = class_1 / class_0
    else:
        ratio_1_0 = None

    print("===== MÔ TẢ TẬP DỮ LIỆU =====")
    print(f"Tổng số mẫu: {total_samples}")
    print(f"Số mẫu lớp 0: {class_0}")
    print(f"Số mẫu lớp 1: {class_1}")

    if ratio_0_1 is not None:
        print(f"Tỷ lệ lớp 0 / lớp 1: {ratio_0_1:.2f}")
    else:
        print("Tỷ lệ lớp 0 / lớp 1: Không tính được vì lớp 1 = 0")

    if ratio_1_0 is not None:
        print(f"Tỷ lệ lớp 1 / lớp 0: {ratio_1_0:.2f}")
    else:
        print("Tỷ lệ lớp 1 / lớp 0: Không tính được vì lớp 0 = 0")

    print("\n===== NHẬN XÉT =====")

    # Đánh giá cân bằng dữ liệu
    if class_0 == 0 or class_1 == 0:
        print("Dữ liệu bị mất cân bằng nghiêm trọng vì chỉ có một lớp hoặc gần như chỉ có một lớp.")
       
    else:
        imbalance_ratio = max(class_0, class_1) / min(class_0, class_1)

        if imbalance_ratio <= 1.2:
            print("Dữ liệu khá cân bằng giữa hai lớp.")
          
        elif imbalance_ratio <= 1.5:
            print("Dữ liệu hơi mất cân bằng nhưng vẫn ở mức chấp nhận được.")
           
        else:
            print("Dữ liệu mất cân bằng.")

# Biểu diễn văn bản với BoW hoặc TF-IDF
def vectorize_text(X_train, X_test, vectorizer_type="bow", ngram_range=(1, 1)):
    if vectorizer_type == "bow":
        vectorizer = CountVectorizer(ngram_range=ngram_range)
    elif vectorizer_type == "tfidf":
        vectorizer = TfidfVectorizer(ngram_range=ngram_range)
    else:
        raise ValueError("Vectorizer type must be 'bow' or 'tfidf'.")

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    return X_train_vec, X_test_vec, vectorizer

# Đánh giá mô hình
def evaluate_and_print(model_name, vectorizer_name, y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label=1, zero_division=0)
    rec = recall_score(y_true, y_pred, pos_label=1, zero_division=0)
    f1 = f1_score(y_true, y_pred, pos_label=1, zero_division=0)
    cm = confusion_matrix(y_true, y_pred)
    
    print(f"Model: {model_name}, Vectorizer: {vectorizer_name}")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print("Confusion Matrix:")
    print(cm)
    print(classification_report(y_true, y_pred))

# Huấn luyện và đánh giá các mô hình
def train_and_evaluate_models(X_train, X_test, y_train, y_test):
    # 1. Multinomial Naive Bayes với BoW và TF-IDF
    for vectorizer_type in ["bow", "tfidf"]:
        print(f"\n#### Bước 1: MULTINOMIAL NAIVE BAYES với {vectorizer_type.upper()} ####")
        X_train_vec, X_test_vec, _ = vectorize_text(X_train, X_test, vectorizer_type=vectorizer_type)
        
        nb_model = MultinomialNB()
        nb_model.fit(X_train_vec, y_train)
        y_pred_nb = nb_model.predict(X_test_vec)
        evaluate_and_print("MultinomialNB", vectorizer_type.upper(), y_test, y_pred_nb)

    # 2. Logistic Regression với BoW và TF-IDF
    for vectorizer_type in ["bow", "tfidf"]:
        print(f"\n#### Bước 2: LOGISTIC REGRESSION với {vectorizer_type.upper()} ####")
        X_train_vec, X_test_vec, _ = vectorize_text(X_train, X_test, vectorizer_type=vectorizer_type)
        
        lr_model = LogisticRegression(max_iter=1000)
        lr_model.fit(X_train_vec, y_train)
        y_pred_lr = lr_model.predict(X_test_vec)
        evaluate_and_print("LogisticRegression", vectorizer_type.upper(), y_test, y_pred_lr)

    # 3. Support Vector Machine với BoW và TF-IDF
    for vectorizer_type in ["bow", "tfidf"]:
        print(f"\n#### Bước 3: SUPPORT VECTOR MACHINE với {vectorizer_type.upper()} ####")
        X_train_vec, X_test_vec, _ = vectorize_text(X_train, X_test, vectorizer_type=vectorizer_type)
        
        svm_model = SVC()
        svm_model.fit(X_train_vec, y_train)
        y_pred_svm = svm_model.predict(X_test_vec)
        evaluate_and_print("SVM", vectorizer_type.upper(), y_test, y_pred_svm)


def main():
    file_path = "filtered_articles.json"  # file đã lọc và gán nhãn
    data = load_json_data(file_path)
    describe_dataset(data)
     # Chuẩn bị dữ liệu
    X = [article['content_tokenized'] for article in data]  # Lấy content làm feature
    y = [article['label'] for article in data]    # Lấy label

    # Chia dữ liệu thành train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Huấn luyện và đánh giá các mô hình
    train_and_evaluate_models(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()