from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    temperature=0,
    model_name="deepseek/deepseek-r1-zero:free",
    openai_api_key="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",
    openai_api_base="https://openrouter.ai/api/v1"
)

print(llm.predict("What’s a good workout for beginners at home?"))
