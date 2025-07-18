from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# OllamaLLM model llama3
model = OllamaLLM(model="llama3")

# Defining the Prompt Template
machine_learning_template = """You are a highly knowledgeable machine learning expert and a completely obsessed with **cats**...
Here is a question:
{input}"""

data_analysis_template = """You are a skilled data analyst,.... respond in json format...
Here is a question:
{input}"""

prompt_infos = [
    {"name": "machine learning", 
     "description": "Good for ML questions", 
     "prompt_template": machine_learning_template},
    {"name": "data analysis", 
     "description": "Good for data analysis", 
     "prompt_template": data_analysis_template}
]

# Mapa para acceder fácilmente a los templates por nombre
template_map = {
    "machine learning": machine_learning_template,
    "data analysis": data_analysis_template
}

# Template que usará el router para decidir qué tipo de prompt usar
MULTI_PROMPT_ROUTER_TEMPLATE = """
You are a router that decides which specialized expert should answer a question.

Available experts:
{destinations}

Given the user query: "{input}", choose the most appropriate expert from the above list.
If none match the intent, return: "fallback"

Your output must be exactly one of the following (without quotes):
{options}

Return ONLY the name, no explanation.
"""

# 
# Crear string con nombres y descripciones
destinations_str = "\n".join(
    [f"{p['name']}: {p['description']}" for p in prompt_infos]
)

options_str = "\n".join([f"{p['name']}" for p in prompt_infos]) + "\nfallback"

router_prompt = PromptTemplate.from_template(MULTI_PROMPT_ROUTER_TEMPLATE)
output_parser = StrOutputParser()

router_chain = (
    {
        "input": lambda x: x["input"],
        "destinations": lambda _: destinations_str,
        "options": lambda _: options_str
    }
    | router_prompt
    | model
    | output_parser
)


# Crear cadenas especializadas
destination_chains = {
    name: PromptTemplate.from_template(template) | model | StrOutputParser()
    for name, template in template_map.items()
}

# Fallback para intents no reconocidos
fallback_template = """You are a helpful assistant. The user question might not fit any specific category.
Do your best to help:
{input}"""

fallback_chain = PromptTemplate.from_template(fallback_template) | model | StrOutputParser()

# Función principal de enrutamiento
valid_destinations = list(destination_chains.keys())

def route(input):
    destination_raw = router_chain.invoke({"input": input})
    destination = destination_raw.lower().strip()

    print(f"\nRouted to (raw): {destination_raw}")
    print(f"Normalized destination: {destination}")

    if destination not in valid_destinations:
        print("No matching expert found. Using fallback.\n")
        return fallback_chain.invoke(input)

    chain = destination_chains[destination]
    return chain.invoke(input)



# Encapsular en función reutilizable
def process_query(user_input):
    return route(user_input)

# CLI interactiva
def main():
    print("\nPrompt Router CLI")
    print("Type 'exit' or 'quit' to leave.\n")
    while True:
        user_input = input("User: ")
        if user_input.lower().strip() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        answer = process_query(user_input)
        print(f"Assistant: {answer}\n")

# Ejecutar si es main
if __name__ == "__main__":
    main()
 
 
