import ollama
import chromadb
from chromadb.config import Settings
import pandas as pd

def chromaDB_initialize():
    client = chromadb.PersistentClient(path="./ChromaDB", settings=Settings(allow_reset=True))
    exist_collections = True
    if "NTUAI" in [c.name for c in client.list_collections()]:
        exist_collections = False
    collection = client.get_or_create_collection(name='NTUAI', metadata={"hnsw:space": "cosine"})
    
    if exist_collections == False:
        advices_data = pd.read_csv("../data/advices.csv")

        # 將各列轉換為 NumPy 陣列
        name_list = advices_data['name'].to_numpy()
        type_list = advices_data['type'].to_numpy()
        catog_list = advices_data['catog'].to_numpy()
        advice_type_list = advices_data['advice_type'].to_numpy()
        reason_advice_list = advices_data['reason/advice'].to_numpy()

        for num in range(0, name_list.shape[0]):
            # store each document in a vector embedding database
            response = embedding_generate(name_list[num] + " " + type_list[num] + " " + catog_list[num] + " " + advice_type_list[num] + " " +  reason_advice_list[num])
            embedding = response["embedding"]
            print("embedding", embedding)
            collection.add(
                ids=[str(num)],
                embeddings=[embedding],
                documents=[name_list[num] + " " + type_list[num] + " " + catog_list[num] + " " + advice_type_list[num] + " " +  reason_advice_list[num]]
            )
    
def embedding_generate(content):
    return ollama.embeddings(
    model='mxbai-embed-large',
    prompt=content,
    )

def retrieve_advices(query):
    client = chromadb.PersistentClient(path="./ChromaDB", settings=Settings(allow_reset=True))
    collection = client.get_or_create_collection(name='NTUAI', metadata={"hnsw:space": "cosine"})
    
    # generate an embedding for the prompt and retrieve the most relevant doc
    response = embedding_generate(query)
    
    results = collection.query(
    query_embeddings=[response["embedding"]],
    n_results=1
    )
    
    data = results['documents'][0][0]
    
    return data