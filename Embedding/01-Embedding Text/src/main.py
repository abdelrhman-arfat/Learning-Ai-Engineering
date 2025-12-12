from service.models.JinaService import JinaService
from service.FakeDB import FakeDB
from concurrent.futures import ThreadPoolExecutor, as_completed

db = FakeDB()
jina = JinaService()

# Add some fake data
sentences = [
    "I love programming",
    "The weather is nice today",
    "AI engineering is the future",
    "Python is my favorite language"
]


def process_and_add(sentence):
    emb = jina.extract_data(sentence)["embeddings"][0]
    db.add(sentence, emb)
    return sentence


with ThreadPoolExecutor(max_workers=4) as executor:  # 4 threads
    futures = [executor.submit(process_and_add, s) for s in sentences]
    for future in as_completed(futures):
        print(f"Added: {future.result()}")

query = "Software development"
query_emb = jina.extract_data(query)["embeddings"][0]

results = db.search(query_emb, top_k=2)
for text, score in results:
    print(f"{text} — {score}")
