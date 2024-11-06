# LAB-GA-For-Business-Aplicattions-Building-Smart-Business-Solutions-with-Langflow-and-Langchain

![Langflow Logo](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

## Introduction

Welcome to the **Langflow and Langchain** lab! In this session, you will learn to create two distinct conversational AI applications using these powerful frameworks. This lab is divided into two parts:

1. **Langflow**: Build a virtual assistant chatbot and practice prompt engineering with **Ollama** as the model backend.
2. **Langchain**: Develop a router to switch between different conversational templates based on the user's intent, enabling specialized responses for different fields.

By the end of this lab, you will have practical experience using these tools for real-world applications.

---

## Initial Setup

### Requirements

1. Fork and clone the provided GitHub repository into your workspace.
2. Install the required libraries using the `requirements.txt` file.
3. Ensure you have **Ollama** installed and running locally.

- [Install Ollama]([https://ollama.ai/docs/installation](https://ollama.com/download))

### Tools Overview

- **Langflow**: A visual editor for designing conversation flows.
- **Langchain**: A modular framework for building AI-powered applications.

---

## Part 1: Virtual Assistant with Langflow

In this part, you will design a virtual assistant using **Langflow**. The assistant will:
- Answer common user queries.
- Use **prompt engineering** to optimize the responses from **Ollama**.

### Scenario

You are tasked with building a virtual assistant for an online bookstore. The assistant should:
1. Answer questions about store hours, book recommendations, and order status.
2. Use a well-crafted prompt to enhance the assistant's conversational quality.

---

### Iteration 1: Setting Up Langflow

1. Launch Langflow locally.
2. Access the Langflow interface in your browser.
3. Import the provided starter flow: `bookstore_assistant.json`.

---

### Iteration 2: Designing the Conversation Flow

1. Add nodes to capture user queries and process the input using **Ollama Chat**.
2. Customize the prompt to provide context for the assistant, such as being helpful and concise.
3. Create response paths for store hours, book recommendations, and order status.
4. Test the flow to ensure it functions as intended.

---

### Iteration 3: Optimizing the Prompt

1. Experiment with different prompts to improve response accuracy and tone.
2. Save and export the updated flow for submission.

---

## Part 2: Specialized Response Routing with Langchain

In this part, you will build a router that directs user queries to specialized templates. Each template will guide **Ollama** to respond as an expert in a specific field.

### Scenario

You are building an AI system for a tech company. The system should:
- Route user queries to specialists in programming, data analysis, or machine learning.
- Provide accurate and contextually appropriate responses.

---

### Iteration 1: Setting Up Langchain

1. Create a new Python file for the Langchain-based chatbot.
2. Set up the necessary components to build a router.

---

### Iteration 2: Defining Templates

1. Create templates for different domains:
   - Programming: Provide detailed programming-related explanations.
   - Data Analysis: Offer insights for data-related problems.
   - Machine Learning: Respond to ML-specific queries.

2. Integrate these templates into the routing system.

---

### Iteration 3: Building the Router

1. Define a routing mechanism to dynamically redirect queries to the appropriate template.
2. Test the router with example queries to ensure it delivers domain-specific responses.

---

### Iteration 4: Adding Intent Detection

1. Implement a basic intent detection mechanism to identify the user's query context.
2. Use the detected intent to route queries dynamically.

---

## Bonus Challenge: Combine Langflow and Langchain

For an advanced challenge, integrate Langchain's routing mechanism into a Langflow-designed flow to create a hybrid conversational AI system.

---

## Submission

1. Push the Langflow JSON file and Langchain Python script to your GitHub repository.
2. Create a Pull Request with a description of your implementations.

---

## Additional Resources

- [Langflow Documentation](https://docs.langflow.com/)
- [Langchain Documentation](https://docs.langchain.com/)
- [Ollama Installation Guide](https://ollama.ai/docs/installation)

![Happy Coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
