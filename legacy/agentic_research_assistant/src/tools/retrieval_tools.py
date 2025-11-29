from utils.vectorstore import vector_store

def retrieve(query):
  """Retrieve information related to a query."""
  retrieved_docs = vector_store.similarity_search(query, k=2)
  return retrieved_docs