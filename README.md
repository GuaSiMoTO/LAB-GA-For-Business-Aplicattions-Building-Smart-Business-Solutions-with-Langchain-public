# LAB: Mastering Langflow and Langchain for Advanced Conversational AI

![Langflow Logo](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

## Introduction

¡Bienvenido al laboratorio de **Langchain**! En este ejercicio, diseñarás un asistente virtual con memoria que proporciona respuestas contextuales y mantiene el historial de conversación.  

Trabajarás dentro de un **Jupyter Notebook**, donde configurarás cadenas especializadas y plantillas de prompts para enrutar consultas a través de diferentes dominios. Este laboratorio práctico te proporcionará las habilidades necesarias para construir asistentes de IA sólidos y basados en código, capaces de gestionar interacciones complejas con facilidad.  

---

## Initial Setup

### Requirements

1. Fork and clone the provided GitHub repository into your workspace.
2. Install the required libraries listed in the `requirements.txt` file.
3. Ensure you have **Ollama** installed and running locally.

### Tools Overview

- **Langchain**: A modular framework for building AI-powered applications.

---

### Iteration 1: Setting Up Langchain

1. Initialize a new Python project and install the necessary dependencies for Langchain and Ollama.
2. Configure the **Ollama** model as the language model for the project.
3. Verify that the **Ollama** model is working correctly by generating a response to a simple prompt.

---

### Iteration 2: Defining Templates and Destination Chains

1. Create specialized templates for domains such as machine learning and data analysis. Use the examples provided for guidance.

```
machine_learning_template = """You are a highly knowledgeable machine learning expert. \
You are excellent at answering questions about algorithms, implementation techniques, \
and best practices in machine learning. \
When you don't know the answer to a question, admit that you don't know.

Here is a question:
{input}"""

data_analysis_template = """You are a skilled data analyst. \
You excel at explaining data analysis techniques, visualizations, and insights. \
Your answers are clear, practical, and based on real-world scenarios. \
If you don't know the answer to a question, say that you don't know.

Here is a question:
{input}"""
```
2. Organize the templates using a structure that includes the name, description, and template content for each domain.

```
prompt_infos = [
    {
        "name": "machine learning",
        "description": "Good for answering questions about machine learning",
        "prompt_template": machine_learning_template
    },
    {
        "name": "data analysis",
        "description": "Good for answering questions about data analysis",
        "prompt_template": data_analysis_template
    }
]
```

3. Map each template to a **destination chain**.
4. Define a default chain to handle queries that do not match any specific domain.

---

### Iteration 3: Setting Up the Multi-Prompt Router

1. Create a `MULTI_PROMPT_ROUTER_TEMPLATE` to guide the model in selecting the appropriate template based on the user’s query. Ensure the template specifies the format for the output as a JSON object with `destination` and `next_inputs` keys.
2. Generate the descriptions for the candidate prompts to include in the multi-prompt template.
3. Define the router prompt using the template and configure it with an output parser.
4. Create the router chain that processes user queries using the defined prompt and logic.

---

### Iteration 4: Implementing Routing Logic

1. Use the router chain to determine the appropriate destination for each query.
2. Implement logic to execute the corresponding chain based on the `destination` returned by the router.
3. Add fallback logic to use the default chain if the destination is not recognized.

---

### Iteration 5: Testing the Router

1. Test the router by providing a variety of queries to the system, covering different domains and edge cases.
2. Verify that each query is routed to the correct domain template and generates an appropriate response.
3. Debug and refine the router logic if any queries are misrouted.

---

## Testing and Expected Outputs

### Langflow Assistant
- Handles multi-turn conversations seamlessly.
- Retains context from earlier interactions to provide personalized and consistent responses.
- Example:
  - **User**: "Can you recommend a sci-fi book?"
  - **Assistant**: "Sure, I recommend 'Dune' by Frank Herbert."
  - **User**: "What other sci-fi books do you recommend?"
  - **Assistant**: "You might also enjoy 'Neuromancer' by William Gibson."

### Langchain Router
- Provides domain-specific responses by routing queries to specialized templates.
- Example:
  - **User**: "What is cross-validation in machine learning?"
  - **Assistant**: "Cross-validation is a technique for assessing the performance of a machine learning model by splitting the dataset into training and testing sets."

---

## Submission

1. Push your completed Langflow JSON file and Langchain script to your GitHub repository.
2. Create a Pull Request with a description of your implementations.

---

## Additional Resources

- [Langflow Documentation](https://docs.langflow.com/)
- [Langchain Documentation](https://docs.langchain.com/)
- [LangChain Ollama Installation Guide](https://python.langchain.com/docs/integrations/llms/ollama/)

![Happy Coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
