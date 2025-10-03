import uuid
import sys

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader

class SingleDocIngestor:
    def __init__(self):
        try:
            self.log = CustomLogger().get_logger(__file__)
        except Exception as e:
            self.log.error(f"Error in SingleDocIngestor __init__: {e}")
            raise DocumentPortalException("Error initializing SingleDocIngestor", sys)
    
    def ingest_files(self):
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in ingest_files: {e}")
            raise DocumentPortalException("Error in ingest_files method", sys)
        
    def create_retriever(self):
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in create_retriever: {e}")
            raise DocumentPortalException("Error in create_retriever method", sys)
        
    

