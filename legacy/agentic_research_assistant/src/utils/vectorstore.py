import faiss
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.document_loaders import PyMuPDFLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
embedding_dim = len(embeddings.embed_query("hello"))
index = faiss.IndexFlatL2(embedding_dim)

vector_store = FAISS(
    embedding_function=embeddings, 
    index=index, 
    docstore=InMemoryDocstore(), 
    index_to_docstore_id={}
)

file_path = r"src/utils/docs/1. Foundational Large Language models & text generation.pdf"
web_path = "https://lilianweng.github.io/posts/2023-06-23-agent/"

doc_loader = PyMuPDFLoader(file_path)
web_loader = WebBaseLoader(
    web_paths=(web_path,), 
)

uploaded_docs = doc_loader.load()
web_docs = web_loader.load()
docs = uploaded_docs + web_docs

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

_ = vector_store.add_documents(documents=all_splits)