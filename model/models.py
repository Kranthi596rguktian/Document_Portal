from enum import Enum
from pydantic import BaseModel, Field, RootModel
from typing import Optional, List, Dict, Any

class Metadata(BaseModel):
    Summary: List[str] = Field(None, description="A brief summary of the document.")
    Title: Optional[str] = Field(None, description="The title of the document.")
    DateCreated : Optional[str] = Field(None, description="The date the document was created.")
    Keywords: Optional[List[str]] = Field(None, description="List of keywords associated with the document.")
    Skills: Optional[List[str]] = Field(None, description="List of skills mentioned in the document.")
    Experience: Optional[List[str]] = Field(None, description="List of experiences mentioned in the document.")
    Education: Optional[List[str]] = Field(None, description="List of educational qualifications mentioned in the document.")
    Certifications: Optional[List[str]] = Field(None, description="List of certifications mentioned in the document.")
    Projects: Optional[List[str]] = Field(None, description="List of projects mentioned in the document.")
    ContactInformation: Optional[Dict[str, Any]] = Field(None, description="Contact information such as email, phone number, address, etc.")
    SocialLinks: Optional[Dict[str, str]] = Field(None, description="Social media or professional profile links.")
    AdditionalInfo: Optional[Dict[str, Any]] = Field(None, description="Any additional information that doesn't fit into the above categories.")
    
    
class ChangeFormat(BaseModel):
    Page: str
    Changes: str
    
class SummaryResponse(RootModel[List[ChangeFormat]]):
    pass

class PromptType(str,Enum):
    DOCUMENT_ANALYSIS = "document_analysis"
    DOCUMENT_COMPARISON = "document_comparison"
    CONTEXTUALIZE_QUESTION = "contextualize_question"
    CONTEXT_QA = "context_qa"

