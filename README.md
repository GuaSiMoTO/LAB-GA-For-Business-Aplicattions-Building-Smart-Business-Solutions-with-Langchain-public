# LAB: Mastering Langflow and Langchain for Advanced Conversational AI

![Langflow Logo](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

## Introduction

Welcome to the **Langflow and Langchain** lab! In this session, you will create two distinct conversational AI applications:

1. **Langflow**: Build a virtual assistant chatbot with memory, prompt engineering, and conversational context management using **Ollama** as the backend model.
2. **Langchain**: Develop a router to switch between different conversational templates based on the user's intent, enabling specialized responses.

By the end of this lab, you will gain practical experience in creating context-aware conversational flows.

---

## Initial Setup

### Requirements

1. Fork and clone the provided GitHub repository into your workspace.
2. Install the required libraries listed in the `requirements.txt` file.
3. Ensure you have **Ollama** installed and running locally.

### Tools Overview

- **Langflow**: A visual editor for designing conversation flows.
- **Langchain**: A modular framework for building AI-powered applications.

---

## Part 1: Virtual Assistant with Langflow

In this part, you will design a virtual assistant with memory that provides contextual responses and maintains conversational history.

---

### Iteration 1: Setting Up Langflow

1. Launch Langflow and access the interface in your browser.
2. Start a new project to design the virtual assistant.

---

### Iteration 2: Adding Chat Input and Memory

1. Add a **Chat Input** node to capture user queries, which will serve as the entry point for interactions.
2. Add a **Memory** node to store conversation history. Configure it to retain recent exchanges or summarize longer conversations.
3. Connect the **Chat Input** node to the **Memory** node to pass user queries through the memory.

---
## Iteration 3: Adding File Input and Parsing Data

1. Add a **File** node to allow the assistant to load the `book_store.json` file. 
   - Configure the **File** node to accept `.json` files.
   - Ensure that the students use the provided `book_store.json` file.

2. Add a **Parse Data** node to process the JSON file.
   - Configure the node to extract and format the list of books from the JSON file.
   - The extracted data should be in a format that can be passed as input to the **Prompt Template** node.

3. Connect the **File** node to the **Parse Data** node to enable the file content to be processed and parsed.

---

### Iteration 4: Adding a Prompt Template

1. Add a **Prompt Template** node to organize the assistant's behavior and responses.
2. Configure the prompt to include:
   - The user's current query.
   - The conversation history stored in memory.
   - The parsed book data from the `book_store.json` file.
3. Connect the **Chat Input** and **Memory** nodes to the **Prompt Template** node.

```
You are a helpful virtual assistant for an online bookstore. Use the following conversation history, the user's current query, and the list of available books to provide accurate and concise responses. If the user asks for book recommendations, suggest books based on previous genres mentioned.
Available Books: {books}
Conversation History: {history}
User Message: {user_message}
AI:
```

---

### Iteration 5: Connecting the Model and Chat Output

1. Add a **Model Node** to process the prompt and generate responses using an Ollama model.
  - Model Name: Use a supported model, such as llama3 or any custom model installed in your Ollama setup.
  - Temperature: Adjust for creative (>0.7) or deterministic (~0.1) outputs.
3. Add a **Chat Output** node to display the assistant's response to the user.
4. Connect the **Prompt Template** node to the **Model Node** and the **Model Node** to the **Chat Output** node.

---

### Iteration 5: Testing the Langflow Assistant

1. Test the flow by interacting with the assistant through the **Chat Input** node.
2. Verify that the assistant retains context and provides personalized, accurate responses based on previous exchanges.

---

## Part 2: Specialized Response Routing with Langchain

In this part, you will build a router that directs user queries to specialized templates. Each template will guide **Ollama** to respond as an expert in a specific field.

---

### Iteration 1: Setting Up Langchain

1. Initialize a new Python project and configure the Langchain environment.
2. Set up a backend to integrate with the **Ollama** model.

---

### Iteration 2: Defining Templates

1. Create templates for specialized domains such as programming, data analysis, and machine learning.
2. Map each intent to a corresponding template for domain-specific responses.

---

### Iteration 3: Building the Router

1. Set up a router to dynamically assign templates based on the user’s query.
2. Configure logic to match user input with the appropriate intent and template.

---

### Iteration 4: Adding Intent Detection

1. Implement a mechanism to detect the user’s intent based on keywords or context.
2. Test the routing system to ensure queries are correctly matched to the appropriate domain template.

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
- [Ollama Installation Guide](https://ollama.ai/docs/installation)

![Happy Coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
