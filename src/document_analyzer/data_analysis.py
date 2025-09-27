import os
import sys
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from prompt import prompt_library

class DocumentAnalyzer:
    """
    Analyzes documents using LLMs and embeddings.
    Automatically logs all actions and supports session-based organization.
    """

    def __init__(self):
        self.log = CustomLogger().get_logger(__name__)
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_model()

            self.parser = JsonOutputParser(pydantic_object=Metadata)
            self.fixing_parser = OutputFixingParser.from_llm(
                llm=self.llm,
                parser=self.parser
            )
            self.prompt = prompt_library.prompt
            self.log.info("Document Analyzer initialized.")

        except Exception as e:
            self.log.error("Error initializing Document Analyzer.", error=str(e))
            raise DocumentPortalException("Failed to initialize Document Analyzer.", sys)


    def analyse_document(self):
        try:
            pass
        except Exception as e:
            self.log.error("Error analyzing document.", error=str(e))
            raise DocumentPortalException("Failed to analyze document.", sys)
