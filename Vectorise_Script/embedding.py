import json
import openai
import tiktoken
import os
from tenacity import retry,wait_fixed

tokenizer = tiktoken.get_encoding("gpt2")



openai.api_key = ""

@retry(wait=wait_fixed(2))
def get_embedding(text, model="text-embedding-ada-002"):
    print("embedding")
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]




canto_path = "srimad-bhagavatam/With Purport/"
vectorized_canto_path = "srimad-bhagavatam/vectorized/"
tokens = 0
for canto_number in range(5,13): #12 cantos in Srimad Bhagavatam
    print("enterint canto",canto_number)
    for file in os.listdir(f"{canto_path}/Canto {canto_number}"):
        print(file)
        with open(f'{canto_path}/Canto {canto_number}/{file}', encoding='utf-8') as fh:
            dataset = json.load(fh)
        embeddings = []
        for verse in dataset:
            chapter_number = file.replace(".json","").replace("Chapter","")
            emb = {
                "id": verse["verse"],
                "devnagari":verse["devanagari"],
                "chapter_number": chapter_number,
                "english_devnagari": verse["english_devnagari"],
                "verse_Syn": verse["verse_Syn"],
                "translation":verse["translation"],
                "purport": verse["purport"],
                "embedding": None
            }
            purport = verse["purport"]
            
            verse_number = verse["verse"]
            translation = verse["translation"]     
            print("canto",canto_number,"chapter",chapter_number,"verse",verse_number)  
                    
            text = f"Shrimd Bhagavatam: Canto {canto_number} Chapter {chapter_number}, Verse {verse_number},{translation},\n purport {purport}"

            tokens += len(tokenizer.encode(text))

            emb["embedding"] = get_embedding(text)
            embeddings.append(emb)

        with open(f'{vectorized_canto_path}/canto_{canto_number}/{file}', "w", encoding="utf-8") as f:
            json.dump(embeddings, f, ensure_ascii=False, indent=4)


print("tokens --->",tokens)
print("cost --->",(tokens/1000)*0.0004)