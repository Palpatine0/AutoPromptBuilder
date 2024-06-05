from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
# To parse string outputs
from langchain_core.output_parsers import StrOutputParser
# Import wait_for_all_tracers to ensure all tracing operations for LangSmith complete before proceeding
from langchain.callbacks.tracers.langchain import wait_for_all_tracers

load_dotenv()

# Ensure all tracing operations are complete before moving on
wait_for_all_tracers()

# Read the contents of the file 'openapi-prompting.txt' into the variable 'text'
with open("openapi-prompting.txt") as f:
    text = f.read()
    # test reading
    print(text[:200])