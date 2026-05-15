from typing import Any, Text, Dict, List
import os
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRecommendMovie(Action):
    def name(self) -> Text:
        return "action_recommend_movie"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        movie_title = tracker.get_slot("movie_title")

        if not movie_title:
            dispatcher.utter_message(text="Please tell me a movie title first.")
            return []

        file_path = os.path.join("movies.csv")

        try:
            movies = pd.read_csv(file_path)
        except FileNotFoundError:
            dispatcher.utter_message(text="Movie dataset not found.")
            return []

        movies["text"] = movies["genres"].fillna("") + " " + movies["description"].fillna("")

        titles_lower = movies["title"].str.lower()
        movie_title_lower = movie_title.lower()

        if movie_title_lower not in titles_lower.values:
            dispatcher.utter_message(
                text=f"Sorry, I cannot find '{movie_title}' in the movie dataset."
            )
            return []

        movie_index = movies[titles_lower == movie_title_lower].index[0]

        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(movies["text"])

        similarity_scores = cosine_similarity(
            tfidf_matrix[movie_index],
            tfidf_matrix
        ).flatten()

        similar_indices = similarity_scores.argsort()[::-1]

        recommendations = []
        for index in similar_indices:
            if index == movie_index:
                continue

            title = movies.iloc[index]["title"]
            score = similarity_scores[index]
            recommendations.append((title, score))

            if len(recommendations) == 3:
                break

        message = f"Movies similar to {movie_title}:\n"
        for title, score in recommendations:
            message += f"- {title} (similarity: {score:.2f})\n"

        dispatcher.utter_message(text=message)

        return []

