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
with open("../openapi-prompting.txt") as f:
    text = f.read()

# Define a template for creating a prompt
template = """
{text}
========================
Based on the above instructions, help me write a good prompt TEMPLATE.

This template should be a string that can be formatted as if python f-string. It can take in any number of variables depending on my objective.

Return your answer in the following format:
```prompt
...
This is my objective:
{objective}
"""

# Create a PromptTemplate instance using the template defined above
prompt = PromptTemplate.from_template(template)
prompt = prompt.partial(text = text)

# Create a chain of operations:
# 1. Use the prompt to generate a structured input.
# 2. Pass the structured input to the ChatOpenAI model (specified as "gpt-4-1106-preview") with a temperature of 0 for deterministic responses.
# 3. Parse the output using StrOutputParser to get a string output.
chain = prompt | ChatOpenAI(model = "gpt-4-1106-preview", temperature = 0) | StrOutputParser()

