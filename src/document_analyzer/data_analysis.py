import os
import sys
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from prompt.prompt_library import PROMPT_REGISTRY

class DocumentAnalyzer:
    """
    Analyzes documents using LLMs and embeddings.
    Automatically logs all actions and supports session-based organization.
    """

    def __init__(self):
        self.log = CustomLogger().get_logger(__name__)
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_llm()

            self.parser = JsonOutputParser(pydantic_object=Metadata)
            self.fixing_parser = OutputFixingParser.from_llm(
                llm=self.llm,
                parser=self.parser
            )
            self.prompt = PROMPT_REGISTRY["document_analysis"]
            self.log.info("Document Analyzer initialized.")

        except Exception as e:
            self.log.error("Error initializing Document Analyzer.", error=str(e))
            raise DocumentPortalException("Failed to initialize Document Analyzer.", sys)


    def analyze_document(self,document_text: str) -> dict:
        """
        Analyzes the document text and extracts metadata and summary.
        """
        try:
            chain = self.prompt | self.llm | self.fixing_parser
            self.log.info("Document analysis chain Initialized.")
            
            response = chain.invoke({
                "format_instructions": self.parser.get_format_instructions(),
                "document_text": document_text
            })
            self.log.info("Metadata extraction completed.", keys=list(response.keys()))
            
            return response
            
        except Exception as e:
            self.log.error("Error analyzing document.", error=str(e))
            raise DocumentPortalException("Failed to analyze document.", sys)