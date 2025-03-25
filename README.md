# LAB-GA-For-Business-Aplicattions-Building-Smart-Business-Solutions-with-Langchain

![Langflow Logo](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

## Objective

Create a prompt router that redirects user questions to specialized templates based on intent, using Langchain and Ollama.

## Requirements

- Jupyter Notebook with installed dependencies.
- Ollama running with an available model.
- Well-documented code in the notebook.


## Iteration 1: Langchain Setup

1. Create an environment with `langchain` and `ollama`.
```pip install langchain_ollama```

2. Test a simple prompt to verify Ollama is working.

## Iteration 2: Create Specialized Templates

Define the following templates:

```python
machine_learning_template = """You are a highly knowledgeable machine learning expert and a completely obsessed with **cats**...
Here is a question:
{input}"""

data_analysis_template = """You are a skilled data analyst,.... respond in json format...
Here is a question:
{input}"""
```

Group them as follows:

```python
prompt_infos = [
    {"name": "machine learning", "description": "Good for ML questions", "prompt_template": machine_learning_template},
    {"name": "data analysis", "description": "Good for data analysis", "prompt_template": data_analysis_template}
]
```

## Iteration 3: Set Up the Router

1. Define `MULTI_PROMPT_ROUTER_TEMPLATE`.
2. Create a parser to interpret the JSON output.
3. Build the routing chain.

## Iteration 4: Routing Logic

1. Use the router to detect the user intent.
2. Execute the corresponding chain based on the result.
3. Implement fallback logic for unrecognized intents.


## Iteration 5: Cli Interface
Use the argparse library or an interactive console loop to receive user input.
```
def main():
    print("Welcome to the prompt router. Type 'exit' or 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        answer = process_query(user_input)
        print("Assistant:", answer)

if __name__ == "__main__":
    main()
```

## Iteration 6: Testing

1. Try several questions:
   - "What is cross-validation in ML?"
   - "How do I visualize categorical data?"
2. Verify that the response comes from the correct template.

## Expected Output

- User: "What is cross-validation in machine learning?"
- Router: Selects `machine_learning_template`.
- Assistant: "Cross-validation is a technique for assessing..."

## Additional Resources

- [Langchain Documentation](https://docs.langchain.com/)
- [LangChain Ollama Installation Guide](https://python.langchain.com/docs/integrations/llms/ollama/)

![Happy Coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)

