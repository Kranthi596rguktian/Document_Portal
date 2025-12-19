# -- Testing Document Analysis

# import os
# from pathlib import Path
# from src.document_analyzer.data_analysis import DocumentAnalyzer
# from src.document_analyzer.data_ingestion import DocumentHandler


# # path to the PDF file
# PDF_PATH = r'C:\Users\Kranthi\OneDrive\Desktop\LLMOPS_Krishnaik\Projects\Project_01\Document_Portal\data\document_analysis\Kranthi_Resume.pdf'

# # Dummy file wrapper to simulate uploaded file (Streamlit style)
# class DummyFile:
#     def __init__(self, file_path):
#         self.name = Path(file_path).name
#         self._file_path = file_path
        
#     def getbuffer(self):
#         return open(self._file_path, 'rb').read()
    
# def main():
#     try:
#         ## Step 1: Data Ingestion
#         print("Starting Data Ingestion...")
#         dummy_pdf = DummyFile(PDF_PATH)
#         handler = DocumentHandler(session_id="test_ingestion_analysis")
#         saved_path = handler.save_pdf(dummy_pdf)
#         print(f"PDF saved at: {saved_path}")
        
#         text_content = handler.read_pdf(saved_path)
#         print(f"Extracted text content from PDF. Number of characters: {len(text_content)}")
        
#         ## Step 2: Data Analysis
#         print("Starting Data Analysis...")
#         analyzer = DocumentAnalyzer()
#         analysis_result = analyzer.analyse_document(document_text=text_content)
        
#         # Step 3: Display Results
#         print("Analysis Result:")
#         for key, value in analysis_result.items():
#             print(f"{key}: {value}")
            
#     except Exception as e:
#         print("Test Failed :  Error during document processing:", str(e))
        
        
# if __name__ == "__main__":
#     main()

# Testing Document Compare
# import io
# from pathlib import Path
# from src.document_compare.data_ingestion import DocumentIngestion
# from src.document_compare.document_comparator import DocumentComparatorLLM

# def load_fake_uploaded_file(file_path:Path):
#     return io.BytesIO(file_path.read_bytes())
    
# def test_compare_documents():
#     ref_path = Path(r"C:\Users\Kranthi\OneDrive\Desktop\LLMOPS_Krishnaik\Projects\Project_01\Document_Portal\data\document_compare\Long_Report_V1.pdf")
#     act_path = Path(r"C:\Users\Kranthi\OneDrive\Desktop\LLMOPS_Krishnaik\Projects\Project_01\Document_Portal\data\document_compare\Long_Report_V2.pdf")

#     class FakeUpload:
#         def __init__(self,file_path:Path):
#             self.name = file_path.name
#             self._buffer = file_path.read_bytes()
            
#         def getbuffer(self):
#             return self._buffer
        
        
#     comparator = DocumentIngestion()
#     ref_upload = FakeUpload(ref_path)
#     act_upload = FakeUpload(act_path)
    
#     ref_file, act_file = comparator.save_uploaded_files(ref_upload,act_upload)
#     combined_text = comparator.combined_documents()
#     comparator.clean_old_sessions(keep_latest=3)
    
#     print("\n Combined Text Preview (First 1000 chars):\n",combined_text[:1000])
    
    
#     llm_comparator = DocumentComparatorLLM()
#     comparision_df = llm_comparator.compare_documents(combined_text)
#     print("\n Comparison Result DataFrame:\n",comparision_df.head())
    
# if __name__ == "__main__":
#     test_compare_documents()

# # -- Testing Single Document Chat
# import sys
# from pathlib import Path
# from langchain_community.vectorstores import FAISS
# from src.single_document_chat.retrieval import ConversationalRAG
# from src.single_document_chat.data_ingestion import SingleDocIngestor
# from utils.model_loader import ModelLoader

# FAISS_INDEX_PATH = Path("faiss_index")
# def test_conversational_rag_on_pdf(pdf_path:str,question:str):
#     try:
#         model_loader = ModelLoader()
        
#         if FAISS_INDEX_PATH.exists():
#             print("Loading existing FAISS index...")
#             embeddings = model_loader.load_embeddings()
#             vectorstore = FAISS.load_local(str(FAISS_INDEX_PATH), embeddings = embeddings,allow_dangerous_deserialization=True)
#             retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
#         else:
#             print("FAISS index not found. Creating a new one...")
#             with open(pdf_path, "rb") as f:
#                 uploaded_files = [f]
#                 ingestor = SingleDocIngestor()
#                 retriever = ingestor.ingest_files(uploaded_files)
#                 print(f"FAISS index created and saved at {FAISS_INDEX_PATH}")
#         session_id = "test_conversational_rag"
#         rag = ConversationalRAG(retriever=retriever, session_id=session_id)
#         response = rag.invoke(user_input=question)
#         print(f"\nQuestion: {question}\nAnswer: {response}")

#     except Exception as e:
#         print("Test Failed :  Error during Conversational RAG processing:", str(e))
#         sys.exit(1)
    

# if __name__ == "__main__":
#     PDF_PATH = r"C:\Users\Kranthi\OneDrive\Desktop\LLMOPS_Krishnaik\Projects\Project_01\Document_Portal\data\single_document_chat\Kranthi_Resume.pdf"
#     QUESTION = "Is it a acceptable for senior datascientist role?"
    
#     if not Path(PDF_PATH).exists():
#         print(f"Test Failed : PDF file not found at {PDF_PATH}")
#         sys.exit(1)
        
#     test_conversational_rag_on_pdf(PDF_PATH,QUESTION)

# ----------------------------

## testing for multidoc chat
import sys
from pathlib import Path
from src.multi_document_chat.data_ingestion import DocumentIngestor
from src.multi_document_chat.retrieval import ConversationRAG

def test_document_ingestion_and_rag():
    try:
        test_files = [
            "data\\multi_doc_chat\\market_analysis_report.docx",
            "data\\multi_doc_chat\\NIPS-2017-attention-is-all-you-need-Paper.pdf",
            "data\\multi_doc_chat\\sample.pdf",
            "data\\multi_doc_chat\\state_of_the_union.txt"
        ]
        
        uploaded_files = []
        
        for file_path in test_files:
            if Path(file_path).exists():
                uploaded_files.append(open(file_path, "rb"))
            else:
                print(f"File does not exist: {file_path}")
                
        if not uploaded_files:
            print("No valid files to upload.")
            sys.exit(1)     
            
        ingestor = DocumentIngestor()
        print('retriever initialized')
        retriever = ingestor.ingest_files(uploaded_files)
        print('retriver created')
        for f in uploaded_files:
            f.close()
            
        session_id = "test_multi_doc_chat"
        
        rag = ConversationRAG(session_id=session_id, retriever=retriever)
        
        question = "what is President Zelenskyy said in their speech in parliament?"
        
        answer=rag.invoke(question)
        
        print("\n Question:", question)
        
        print("Answer:", answer)
        
        if not uploaded_files:
            print("No valid files to upload.")
            sys.exit(1)
            
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise e
        sys.exit(1)

if __name__ == "__main__":
    test_document_ingestion_and_rag()