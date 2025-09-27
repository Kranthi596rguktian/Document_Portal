from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages("""
    You are a highly capab;e assistant trained to analyze and summarize documents.
    Return ONLY valid JSON matching the exact schema below:
    
    {format_instructions}
    
    Analyze this document:
    
    {document_text}
    """)