import json
import openai
openai.api_key = ""
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]
with open('chapter1.json', encoding='utf-8') as fh:
    dataset = json.load(fh)
embeddings = []
for verse in dataset:
    emb = {
        "id": verse["verse"],
        "devnagari":verse["devanagari"],
        "chapter_number": "1",
        "english_devnagari": verse["english_devnagari"],
        "verse_Syn": verse["verse_Syn"],
        "translation":verse["translation"],
        "purport": verse["purport"],
        "embedding": None
    }
    purport = verse["purport"]
    chapter_number = "1"
    verse_number = verse["verse"]
    translation = verse["translation"]
    
             
    text = f"Bhagavad Gita: Chapter {chapter_number}, Verse {verse_number},{translation},{purport}"
    emb["embedding"] = get_embedding(text)
    embeddings.append(emb)

with open("chapter1_vectorised.json", "w", encoding="utf-8") as f:
    json.dump(embeddings, f, ensure_ascii=False, indent=4)
