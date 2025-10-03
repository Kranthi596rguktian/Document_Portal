import sys
import os
from operator import itemgetter
from typing import List, Optional, Dict, Any

from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS

from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import PromptType


class ConversationalRAG:
    def __init__(self):
        try:
            self.log = CustomLogger().get_logger(__file__)
        except Exception as e:
            self.log.error(f"Error in ConversationalRAG __init__: {e}")
            raise DocumentPortalException("Error initializing ConversationalRAG", sys)
        
    def _load_llm(self):
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in _load_llm: {e}")
            raise DocumentPortalException("Error in _load_llm method", sys)
        
    def _get_session_history(self):
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in _get_session_history: {e}")
            raise DocumentPortalException("Error in _get_session_history method", sys)
        
    def load_retriever_from_faiss(self,faiss_index_path:str) -> FAISS:
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in load_retriever_from_faiss: {e}")
            raise DocumentPortalException("Error in load_retriever_from_faiss method", sys)

    def invoke(self):
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in invoke: {e}")
            raise DocumentPortalException("Error in invoke method", sys)