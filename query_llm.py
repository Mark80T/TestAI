from dotenv import load_dotenv
from groq import Groq
import os
import numpy as np

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_question(question, index, texts, top_k=3):
    from build_faiss import get_embedding_from_instructor
    q_emb = get_embedding_from_instructor(question)
    D, I = index.search(np.array([q_emb]).astype("float32"), top_k)
    context = "\n".join([texts[i] for i in I[0]])
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "Sei un assistente esperto in aziende."},
            {"role": "user", "content": f"Contesto: {context}\n\nDomanda: {question}"}
        ]
    )
    return response.choices[0].message.content.strip(), context