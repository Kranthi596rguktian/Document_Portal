import sys
from dotenv import load_dotenv
import pandas as pd
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from prompt.prompt_library import PROMPT_REGISTRY
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from utils.model_loader import ModelLoader


class DocumentComparatorLLM:
    def __init__(self):
        pass
    
    def compare_documents(self):
        """
        Compares two documents and identifies differences.
        """
        pass
    
    def _format_response(self):
        """
        Formats the comparison response.
        """
        pass
    
    
    
    