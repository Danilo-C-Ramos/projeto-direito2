from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from .cria_base import cria_documentos
import os
import time

def search_vector_store(query: str):

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index("clinicas")
    namespace = "credito-consignado"

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # Gerar embedding
    query_vec = embeddings.embed_query(query)

    # ✅ BUSCAR DIRETAMENTE
    res = index.query(
        vector=query_vec,
        top_k=4,
        namespace=namespace,
        include_metadata=True
    )

    resultados_sim = []
    resultados_nao = []

    for match in res["matches"]:
        metadata = match.get("metadata", {})
        label = metadata.get("label")
        texto = metadata.get("text", "")
        score = match.get("score")

        item = {"texto": texto, "score": score}

        if label == "SIM":
            resultados_sim.append(item)
        elif label == "NAO":
            resultados_nao.append(item)


    return resultados_sim, resultados_nao

