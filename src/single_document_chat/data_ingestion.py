import uuid
import sys

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from datetime import datetime, timezone

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader

class SingleDocIngestor:
    def __init__(self,data_dir : str = "data/single_document_chat",faiss_dir : str = "faiss_index"):
        try:
            self.log = CustomLogger().get_logger(__file__)
            self.data_dir = Path(data_dir)
            self.data_dir.mkdir(parents=True, exist_ok=True)
            self.faiss_dir = Path(faiss_dir)
            self.faiss_dir.mkdir(parents=True, exist_ok=True)
            self.model_loader = ModelLoader()
            self.log.info("SingleDocIngestor initialized successfully.")
        except Exception as e:
            self.log.error(f"Error in SingleDocIngestor __init__: {e}")
            raise DocumentPortalException("Error initializing SingleDocIngestor", sys)
    
    def ingest_files(self,uploaded_files):
        try:
            documents = []
            for uploaded_file in uploaded_files:
                unique_filename = f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
                temp_path = self.data_dir / unique_filename
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.read())
                self.log.info("File saved",file=str(temp_path))
                loader = PyPDFLoader(str(temp_path))
                docs = loader.load()
                documents.extend(docs)
            self.log.info(f"Total documents loaded: {len(documents)}")
            return self._create_retriever(documents)
        except Exception as e:
            self.log.error(f"Error in ingest_files: {e}")
            raise DocumentPortalException("Error in ingest_files method", sys)
        
    def _create_retriever(self,documents):
        try:
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = splitter.split_documents(documents)
            self.log.info(f"Total chunks created: {len(chunks)}")
            
            embeddings = self.model_loader.load_embeddings()
            vectorstore = FAISS.from_documents(chunks, embeddings)
            
            # Save the FAISS index
            vectorstore.save_local(str(self.faiss_dir))
            self.log.info("FAISS index saved",path=str(self.faiss_dir))
            
            retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
            self.log.info("Retriever created successfully.",retriever_type=type(retriever).__name__)
        
            return retriever
            
        except Exception as e:
            self.log.error(f"Error in create_retriever: {e}")
            raise DocumentPortalException("Error in create_retriever method", sys)
        
    

