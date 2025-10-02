import os
import sys
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from utils.config_loader import load_config
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)

class ModelLoader:
    """Handles the loading of various models and configurations."""

    def __init__(self):
        """Initialize the ModelLoader with environment variables and configurations."""
        load_dotenv()
        self._validate_env()
        self.config = load_config()
        log.info("Configuration loaded successfully.", config_key = list(self.config.keys()))

    def _validate_env(self):
        """Validate environment variables."""
        required_vars = ["GOOGLE_API_KEY", "GROQ_API_KEY"]
        self.api_keys = {key: os.getenv(key) for key in required_vars}
        missing_vars = [key for key, value in self.api_keys.items() if not value]
        if missing_vars:
            log.error("Missing environment variables: %s", missing_vars)
            raise DocumentPortalException("Missing environment variables",sys)

    def load_embeddings(self):
        try:
            log.info("Loading Google Generative AI Embeddings model.")
            model_name = self.config["embedding"]['model_name']
            return GoogleGenerativeAIEmbeddings(model=model_name)
        except Exception as e:
            log.error("Error loading Embeddings model: %s", e)
            raise DocumentPortalException("Error loading Embeddings model",sys)

    def load_model(self):
        """
        Load and return the LLM model.
        Load LLM dynamically based on provider in config."""

        llm_block = self.config.get("llm", {})
        log.info("Loading LLM model from config: %s", llm_block)
        provider_key = os.getenv("LLM_PROVIDER", "groq")

        if provider_key not in llm_block:
            log.error("Unsupported LLM provider: %s", provider_key)
            raise DocumentPortalException("Unsupported LLM provider",sys)
        
        llm_config = llm_block[provider_key]
        provider = llm_config.get("provider")
        model_name = llm_config.get("model_name")
        temperature = llm_config.get("temperature", 0)
        max_tokens = llm_config.get("max_tokens", 2048)

        log.info("Loading LLM model", provider_key=provider_key, model_name=model_name, temperature=temperature, max_tokens=max_tokens)

        if provider_key == "groq":
            llm = ChatGroq(model=model_name, temperature=temperature, max_tokens=max_tokens, api_key=self.api_keys["GROQ_API_KEY"])
            return llm
        elif provider_key == "google":
            llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature, max_tokens=max_tokens, api_key=self.api_keys["GOOGLE_API_KEY"])
            return llm
        else:
            log.error("Unsupported LLM provider: %s", provider_key)
            raise DocumentPortalException("Unsupported LLM provider",sys)

if __name__ == "__main__":
    loader = ModelLoader()

    embeddings = loader.load_embeddings()
    print("Embeddings model loaded:", embeddings)

    llm = loader.load_llm()
    print("LLM model loaded:", llm)

    #Test the modelloader
    result = llm.invoke(["Hello, how are you?"])
    print("LLM model invocation result:", result.content)