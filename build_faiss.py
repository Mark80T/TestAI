import os
import faiss
import pyodbc
from InstructorEmbedding import INSTRUCTOR
from dotenv import load_dotenv

load_dotenv()
model = INSTRUCTOR("hkunlp/instructor-large")

def get_embedding_from_instructor(text):
    return model.encode([("Represent the company info for retrieval:", text)])[0]

def get_texts_from_db():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=testdb;"
        "UID=llm_user;"
        "PWD=llm_@sdsdb!F_@d85_password_123!"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.aziende_anonime")
    rows = cursor.fetchall()
    texts = [" ".join(str(col) for col in row) for row in rows]
    conn.close()
    return texts

def get_faiss_index():
    texts = get_texts_from_db()
    embeddings = [get_embedding_from_instructor(t) for t in texts]
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index, texts