from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
"all-MiniLM-L6-v2"
)

def validate_similarity(
expected,
actual):

    emb1 = model.encode([expected])
    emb2 = model.encode([actual])

    score = cosine_similarity(
        emb1,
        emb2
    )[0][0]

    return score