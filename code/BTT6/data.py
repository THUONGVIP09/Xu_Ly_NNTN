import json
from collections import defaultdict

# Đọc dữ liệu từ file JSON
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Nhóm bài viết theo topic
def group_by_topic(data):
    topic_count = defaultdict(list)
    for entry in data:
        topic = entry.get("topic", "").strip()
        topic_count[topic].append(entry)
    return topic_count

# Hàm gán nhãn
def assign_label(topic):
    topic_1 = {
        "Kinh tế",
        "Kinh doanh",
        "Tài chính",
        "Thị trường",
        "Chứng khoán"
    }
    return 1 if topic in topic_1 else 0

# Lọc theo đúng số lượng đã chỉ định và thêm label
def filter_articles_by_count(topic_count, topic_limit, output_file):
    filtered_data = []

    # Chỉ lấy đúng các thể loại mà bạn khai báo trong topic_limit
    for topic, max_articles in topic_limit.items():
        articles = topic_count.get(topic, [])
        selected_articles = articles[:max_articles]

        print(f"Thể loại: {topic} | Có sẵn: {len(articles)} | Lấy: {len(selected_articles)}")

        for article in selected_articles:
            article_copy = article.copy()
            article_copy["label"] = assign_label(topic)
            filtered_data.append(article_copy)

    # Lưu kết quả vào file JSON mới
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)

    print(f"\nDữ liệu đã được lưu vào {output_file}")

# =========================
# CHƯƠNG TRÌNH CHÍNH
# =========================

file_path = "news_dataset/news_dataset.json"
output_file = "filtered_articles.json"

data = load_json_data(file_path)
topic_count = group_by_topic(data)

topic_limit = {
    "Kinh tế": 100,
    "Kinh doanh": 100,
    "Tài chính": 150,
    "Thị trường": 200,
    "Chứng khoán": 150,
    "Thể thao": 300,
    "Giải trí": 300,
    "Sức khỏe": 300,
    "Công nghệ": 300,
    "Giáo dục": 300,
    "Du lịch": 300,
    "Ẩm thực": 300,
    "Pháp luật": 300,
    "Xã hội": 300,
}

filter_articles_by_count(topic_count, topic_limit, output_file)