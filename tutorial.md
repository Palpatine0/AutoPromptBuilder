# Building an "Auto-Prompt Builder" using Langing Smith and Lang Serve

## Objective
In this lab, we will build an "Auto-Prompt Builder" application using Langing Smith and Lang serve. This project involves setting up and deploying the project, creating API keys, and debugging with Lang serve.

## Prerequisites
Before starting, ensure you have the following installed on your system:
- Python 3.10 or higher
- pip (Python package installer)
- Git (optional)

### Step 1: Initial Setup

#### Environment Setup
To start, we need to manage sensitive information such as API keys securely. Using a `.env` file is a standard practice for this purpose.

1. **Create a `.env` file:**
   - This file will store your API keys and other configuration settings. Ensure it is included in your `.gitignore` file to prevent it from being committed to your repository.

   Example `.env` file:
   ```plaintext
   OPENAI_API_KEY="your_open_api_key"
   ```
   

2. **Install required packages:**
   - We need several packages for our project: `openai`, `python-dotenv`, `langchain_community`, `langchain`, and `langchain-cli`.

   Commands:
   ```bash
   pip install openai python-dotenv
   ```

   ```bash
   pip install langchain_community langchain
   ```

   ```bash
   pip install -U langchain-cli
   ```

#### Key Concepts

##### 1. Langchain CLI
- **Definition:** The Langchain CLI (Command-Line Interface) is a tool designed to help developers efficiently manage Langchain projects. It provides a variety of commands and utilities to streamline project setup, development, and deployment processes.
- **Installation:** After installing the Langchain CLI, you can use it to perform various tasks related to your Langchain projects. This includes creating new projects, managing dependencies, running development servers, and more.

### Step 2: Setup LangServe

#### LangServe Setup
In this step, we will set up LangServe to manage our application deployment.

1. **Initialize a New LangServe Application:**
   - Use the LangServe CLI to create a new application called `auto-prompt-builder`.

   Command:
   ```bash
   langchain app new auto-prompt-builder
   ```

2. **Folder Structure:**
   - This command sets up the necessary folder structure and configuration files for the application.

#### Key Concepts

##### 1. LangServe
- **Definition:** LangServe is a deployment platform specifically designed for applications built with Langchain. It offers tools to manage, deploy, and debug Langchain applications, making the deployment process more straightforward and integrated.
- **Usage:** 
  
   - Simplified Deployment: Automates the packaging and deployment of Langchain applications with minimal configuration.
   - Management Tools: Provides robust tools for managing deployed applications, including monitoring performance, handling updates, and managing resources.
   - Debugging Tools: Integrated debugging tools to identify and resolve issues quickly, including viewing logs and diagnostics.

### Step 3: Setup LangSmith

#### Access LangSmith
To manage and trace your LangChain projects, we will set up LangSmith. Follow the steps below to get your API key and create a project.

#### 1: Get Your Own API Key
1. **Access LangSmith:**
   - Navigate to [LangSmith](https://smith.langchain.com/).

2. **Navigate to API Keys:**
   - Click on the settings icon in the sidebar to access the settings page.
     <img src="https://i.imghippo.com/files/Xrf9h1717504120.png" alt="" border="0">
   - Go to the "API Keys" section and click on "Create API Key".
     <img src="https://i.imghippo.com/files/K3JnM1717504141.png" alt="" border="0">
   - Provide a description for your API key, select "Personal Access Token", and click "Create API Key".
     <img src="https://i.imghippo.com/files/oyioV1717504162.png" alt="" border="0">

3. **Store the API Key:**
   - Copy the generated API key and store it securely. Add it to your `.env` file:
     ```plaintext
     LANGCHAIN_TRACING_V2=true
     LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
     LANGCHAIN_API_KEY="your_langchain_api_key"
     LANGCHAIN_PROJECT="your_project_name"
     OPENAI_API_KEY="your_open_api_key"
     ```

#### 2: Create a Project
1. **Create a New Project:**
   - From the LangSmith dashboard, click on "New Project".
     <img src="https://i.imghippo.com/files/l0evk1717503570.jpg" alt="" border="0">
   - Enter the project name (`AutoPromptBuilder`) and other details, then click "Submit".
     <img src="https://i.imghippo.com/files/DtxiA1717503612.jpg" alt="" border="0">

#### Additional Setup
1. **Install Required Packages:**
   - Ensure you have the necessary packages installed for LangChain and LangSmith.
     ```bash
     pip install -U langchain langchain-openai
     ```
     
#### Key Concepts

##### 1. LangSmith

- **Definition:** LangSmith is a comprehensive platform tailored for the development, deployment, and monitoring of Langchain applications. It offers an array of tools and services to streamline the lifecycle of Langchain applications from inception to production.

- **Usages:**
  - **Simplified Development:** Provides a suite of tools to facilitate the development of Langchain applications, including templates, libraries, and integration support. 
  - **Management and Monitoring:** Equipped with robust tools for monitoring and managing deployed applications. This includes real-time performance monitoring, resource management, and alerting systems to ensure optimal operation. 
  - **Debugging and Diagnostics:** Advanced debugging tools to quickly identify and resolve issues. Features include detailed logging, tracebacks, and diagnostic reports to maintain application health and performance.



##### 2. LangSmith Environment Variables
By setting these environment variables, you can fully leverage Langchain's tracing capabilities, configure the API endpoint, manage authentication with your API key, and organize your operations under specific projects.

- **`LANGCHAIN_TRACING_V2`**: this variable activates detailed tracing of the operations within your Langchain application. This is particularly useful for debugging and performance monitoring. 
- **`LANGCHAIN_ENDPOINT`**: Set this variable to the URL of the Langchain API endpoint you want to interact with. This can be used to direct your application to the appropriate API server. 
- **`LANGCHAIN_API_KEY`**: Set this variable with your unique API key to authenticate your requests to the Langchain API. The API key is used to ensure secure communication between your application and the Langchain API.
- **`LANGCHAIN_PROJECT`**: Set this variable to the name of your project to organize and manage different Langchain operations under a specific project context. This helps in keeping track of resources and tracing logs specific to a project.
 

 
### Step 4: Add LangChain Setup and Prompt Guidelines

#### LangChain Setup
In this step, we will set up LangChain for prompt engineering and output parsing, and provide guidelines for creating effective prompts.

1. **Create `main.py`:**
   - This script sets up LangChain prompts and output parsing, and loads environment variables from the `.env` file.

   `main.py`:
   ```python
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
   ```
   
    Run the test
    <img src="https://i.imghippo.com/files/TLuxc1717594829.jpg" alt="" border="0">    

2. **Create `openapi-prompting.txt`:**
   - This file contains detailed guidelines and strategies for prompt engineering to get better results from large language models.

   `openapi-prompting.txt`:
   ```plaintext
   Prompt engineering
   This guide shares strategies and tactics for getting better results from large language models (sometimes referred to as GPT models) like GPT-4. The methods described here can sometimes be deployed in combination for greater effect. We encourage experimentation to find the methods that work best for you.

   You can also explore example prompts which showcase what our models are capable of:

   Prompt examples
   Explore prompt examples to learn what GPT models can do
   ...
   ```
   
    Access the file by click the [link](https://github.com/Palpatine0/AutoPromptBuilder/blob/master/openapi-prompting.txt)

#### Key Concepts

##### 1. LangChain Prompts and Output Parsing
- **LangChain Prompts:** Provides a framework for creating structured prompts for language models.
- **Output Parsing:** Ensures that the output from the language model is parsed and formatted correctly.
- **Code Example:**
  ```python
  from langchain_core.prompts import PromptTemplate
  from langchain_core.output_parsers import StrOutputParser
  ```

##### 2. Tracing with LangSmith
- **Purpose:** Ensures all tracing operations are complete before proceeding, which is crucial for debugging and monitoring.
- **Code Example:**
  ```python
  from langchain.callbacks.tracers.langchain import wait_for_all_tracers
  wait_for_all_tracers()
  ```

##### 3. Prompt Engineering Guidelines
- **Purpose:** Provides strategies and tactics for creating effective prompts to get better results from large language models.
- **Usage:** Includes detailed instructions and examples for writing clear and effective prompts.



### Step 5: Add Prompt Template Creation and Streaming Response Chain

#### LangChain Prompt Template and Streaming Response
In this step, we add the functionality to create prompt templates and generate responses using a streaming response chain.

1. **Update `main.py`:**
   - Add code to read and process content from `openapi-prompting.txt`.
   - Define a prompt template for creating structured input with partial application of text.
   - Create a chain to generate and parse output using `ChatOpenAI` and `StrOutputParser` with streaming response.
   - Add task objective and invoke the chain to stream the output.

   Updated `main.py`:
   ```python
   from langchain_core.prompts import PromptTemplate
   from langchain_community.chat_models import ChatOpenAI
   from dotenv import load_dotenv
   from langchain_core.output_parsers import StrOutputParser
   from langchain.callbacks.tracers.langchain import wait_for_all_tracers

   load_dotenv()

   # Ensure all tracing operations are complete before moving on
   wait_for_all_tracers()

   # Read the contents of the file 'openapi-prompting.txt' into the variable 'text'
   with open("openapi-prompting.txt") as f:
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
   prompt = prompt.partial(text=text)

   # Create a chain of operations:
   # 1. Use the prompt to generate a structured input.
   # 2. Pass the structured input to the ChatOpenAI model (specified as "gpt-4-1106-preview") with a temperature of 0 for deterministic responses.
   # 3. Parse the output using StrOutputParser to get a string output.
   chain = prompt | ChatOpenAI(model="gpt-4-1106-preview", temperature=0) | StrOutputParser()

   # Define a task objective
   task = "answer a question based on context provided, and ONLY on that context."

   # Invoke the chain with the objective and the text read from the file as inputs
   for token in chain.stream({"objective": task}):
       print(token, end="")
   ```
   
    Run the test
    <img src="https://i.imghippo.com/files/hUTgb1717598567.jpg" alt="" border="0">
    Your LangSmith now should have successfully tracking your prompt.
    <img src="https://i.imghippo.com/files/vDpOM1717598770.jpg" alt="" border="0">

#### Key Concepts

##### 1. Prompt Templates
- **Definition:** A structured way to create prompts for language models, allowing for dynamic input variables.
- **Usage:** Templates are defined as strings that can be formatted using Python f-strings.
- **Code Example:**
  ```python
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
  ```

##### 2. Partial Application of Templates
- **Definition:** A technique where part of the template is pre-filled with specific values, allowing for reuse with different dynamic inputs.
- **Usage:** The `partial` method is used to pre-fill part of the template.
- **Code Example:**
  ```python
  prompt = prompt.partial(text=text)
  ```

##### 3. Streaming Response Chain
- **Definition:** A chain of operations that processes input through multiple stages and generates a streaming response.
- **Usage:** The chain combines prompt generation, model invocation, and output parsing.
- **Code Example:**
  ```python
  chain = prompt | ChatOpenAI(model="gpt-4-1106-preview", temperature=0) | StrOutputParser()
  ```

##### 4. Task Objectives
- **Definition:** Clear and specific goals that guide the generation of prompts and responses.
- **Usage:** Task objectives are passed as inputs to the chain to generate context-specific outputs.
- **Code Example:**
  ```python
  task = "answer a question based on context provided, and ONLY on that context."
  ```

### Step 6: Integrate Prompt Generation Chain with FastAPI and Setup LangServe

In this step, we integrate our prompt generation chain with a FastAPI server and set up LangServe for serving the application.

#### 1. FastAPI Integration

1. **Create `chain.py` in the `auto-prompt-builder/app` directory:**
   - Define a prompt template and chain for generating structured input and parsing output.
   - Load environment variables and read content from `openapi-prompting.txt`.

   ```python
   from langchain_core.prompts import PromptTemplate
   from langchain_community.chat_models import ChatOpenAI
   from dotenv import load_dotenv
   from langchain_core.output_parsers import StrOutputParser
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
   prompt = prompt.partial(text=text)

   # Create a chain of operations:
   # 1. Use the prompt to generate a structured input.
   # 2. Pass the structured input to the ChatOpenAI model (specified as "gpt-4-1106-preview") with a temperature of 0 for deterministic responses.
   # 3. Parse the output using StrOutputParser to get a string output.
   chain = prompt | ChatOpenAI(model="gpt-4-1106-preview", temperature=0) | StrOutputParser()
   ```

2. **Update `server.py` in the `auto-prompt-builder/app` directory:**
   - Integrate the chain with FastAPI.
   - Add a route to serve the chain.

   ```python
   from fastapi import FastAPI
   from fastapi.responses import RedirectResponse
   from langserve import add_routes
   from app.chain import chain

   app = FastAPI()

   @app.get("/", include_in_schema=False)
   async def redirect_root_to_docs():
       return RedirectResponse(url="/docs")

   # Edit this to add the chain you want to add
   add_routes(app, chain, path="/prompter")

   if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)
   ```

3. **Move `openapi-prompting.txt` to the `auto-prompt-builder/` directory:**
   - Ensure that `openapi-prompting.txt` is located in the correct directory for reading.


### Step 7: Serve the Application Using LangServe

#### 1. Serving the Application by LangServe
   - Run the following commands to set up and serve the application using LangServe.

   ```bash
   cd auto-prompt-builder
   langchain serve
   ```

Access [Prompter Playground](http://127.0.0.1:8000/prompter/playground/), be note that the port may vary depending on the configuration.

#### Key Concepts

##### 1. FastAPI
- **Definition:** FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Usage:** Used to create a web server to host the LangChain application.
- **Code Example:**
  ```python
  from fastapi import FastAPI
  app = FastAPI()
  ```

##### 2. LangServe
- **Definition:** LangServe is a tool for deploying and serving LangChain applications.
- **Usage:** Used to serve the application and manage the API endpoints.
- **Code Example:**
  ```bash
  langchain serve
  ```
 