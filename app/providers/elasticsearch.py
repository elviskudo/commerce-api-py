from elasticsearch import Elasticsearch
import os

ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")

es_client = Elasticsearch([ELASTICSEARCH_URL])

# Contoh untuk menambahkan dokumen ke Elasticsearch
def add_document(index: str, doc_type: str, document: dict):
    es_client.index(index=index, doc_type=doc_type, body=document)

# Contoh untuk pencarian dokumen
def search_document(index: str, query: dict):
    return es_client.search(index=index, body=query)