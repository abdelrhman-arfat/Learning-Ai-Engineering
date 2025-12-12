import numpy as np


class FakeDB:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, text, embedding):
        """
        text: النص الأصلي
        embedding: list/array of floats
        """
        self.texts.append(text)
        self.vectors.append(np.array(embedding))

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query_embedding, top_k=3):
        query_embedding = np.array(query_embedding)

        similarities = []
        for idx, vector in enumerate(self.vectors):
            score = self.cosine_similarity(query_embedding, vector)
            similarities.append((self.texts[idx], score))

        # sort by similarity desc
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]
