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
        load_dotenv()
        self.log = CustomLogger().get_logger(__name__)
        self.loader = ModelLoader()
        self.llm = self.loader.load_model()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser,llm=self.llm)
        self.prompt = PROMPT_REGISTRY['document_comparison_prompt']
        self.chain = self.prompt | self.llm | self.pasrser | self.fixing_parser
        
        self.log.info("DocumentComparatorLLM initialized successfully.")
    
    def compare_documents(self):
        """
        Compares two documents and identifies differences.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in compare_documents: {e}")
            raise DocumentPortalException("Error occurred while comparing documents.",sys)
    
    def _format_response(self):
        """
        Formats the comparison response.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in _format_response: {e}")
            raise DocumentPortalException("Error occurred while formatting response.",sys)
    
    
    
    