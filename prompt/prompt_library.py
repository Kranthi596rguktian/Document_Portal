from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a highly capable assistant trained to analyze and summarize documents. Return ONLY valid JSON matching the exact schema below:\n\n{format_instructions}"),
    ("human", "Analyze this document:\n\n{document_text}")
])