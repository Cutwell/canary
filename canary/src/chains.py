from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

with open("canary/src/prompts/chatbot.txt", "r") as file:
    chatbot_prompt_template = file.read()

with open("canary/src/prompts/integrity.txt", "r") as file:
    integrity_prompt_template = file.read()

chatbot_llm = OpenAI(temperature=0)
chatbot_llm_chain = LLMChain(
    llm=chatbot_llm,
    prompt=PromptTemplate.from_template(chatbot_prompt_template)
)

integrity_llm = OpenAI(temperature=0)
integrity_llm_chain = LLMChain(
    llm=integrity_llm,
    prompt=PromptTemplate.from_template(integrity_prompt_template)
)
