from langchain_groq import ChatGroq

api_key = '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'





llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key = api_key
    # other params...
)
resp = llm.invoke("first person on moon was....")

print(resp.content)