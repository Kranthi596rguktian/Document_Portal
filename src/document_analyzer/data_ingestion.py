import os
import fitz
import uuid
from datetime import datetime
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from langchain_community.document_loaders import PyPDFLoader  

class DocumentHandler:
    """
    Handles PDF saving and reading operations.
    Automatically logs all actions and supports session-based organization.
    """

    def __init__(self,data_dir=None,session_id=None):

        try:
            self.log = CustomLogger().get_logger(__name__)
            self.data_dir = data_dir or os.getenv(
                "DATA_STORAGE_PATH",
                os.path.join(os.getcwd(),"data","document_analysis")
            )
            self.session_id = session_id or f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(uuid.uuid4())[:8]}"

            self.session_path = os.path.join(self.data_dir, self.session_id)
            os.makedirs(self.session_path, exist_ok=True)
            self.log.info("PDF Handler initialized.",session_id=self.session_id,session_path=self.session_path)

        except Exception as e:
            self.log.error("Error initializing PDF Handler.", error=str(e))
            raise DocumentPortalException("Failed to initialize PDF Handler.", e) from e

    def save_pdf(self, uploaded_file):
        filename = os.path.basename(uploaded_file.name)

        if not filename.lower().endswith('.pdf'):
            raise DocumentPortalException("Invalid file type. Only PDF files are allowed.")

        save_path = os.path.join(self.session_path, filename)

        with open(save_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        self.log.info("PDF saved successfully.", filename=filename,
            save_path=save_path, session_id=self.session_id)
        return save_path

    def read_pdf(self,pdf_path):
        try:
            # text_chunks = []
            # with fitz.open(pdf_path) as doc:
            #     for page_num, page in enumerate(doc, start = 1):
            #         text_chunks.append(f"--- Page {page_num} ---\n{page.get_text()}\n")
            # text = "\n".join(text_chunks)
            loader = PyPDFLoader(pdf_path)
            pages = []
            for page in loader.load():
                pages.append(page)
            self.log.info("PDF read successfully.", filename=os.path.basename(pdf_path), session_id=self.session_id)
            return pages
        except Exception as e:
            self.log.error("Error reading PDF.", error = str(e), session_id=self.session_id)
            raise DocumentPortalException("Failed to read PDF.", e) from e

if __name__ == "__main__":
    from io import BytesIO
    from pathlib import Path

    pdf_path = r"C:\Users\Kranthi\OneDrive\Desktop\LLMOPS_Krishnaik\Projects\Project_01\Document_Portal\data\document_analysis\Kranthi_Resume.pdf"

    class DummyFile:
        def __init__(self, path):
            self.name = os.path.basename(path)
            self.path = path

        def getbuffer(self):
            with open(self.path, 'rb') as f:
                return f.read()

    dummy_file = DummyFile(pdf_path)
    handler = DocumentHandler(session_id="test_session")

    try:
        saved_path = handler.save_pdf(dummy_file)
        print(saved_path)

        pages = handler.read_pdf(saved_path)
        print("PDF Content:")
        print(pages[0].page_content[:500])  # Print first 500 characters
    except Exception as e:
        print(f"Error: {e}")
