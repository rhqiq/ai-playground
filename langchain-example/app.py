from dotenv import load_dotenv
import os

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize the model with API key
model = init_chat_model(
    "gemini-2.0-flash",
    model_provider="google_genai",
    google_api_key=os.getenv("GEMINI_API_KEY")  # Get API key from environment variable
)

# Method 1: Using tuples (works)
prompt_template1 = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me a joke about {topic}")
])


# Both methods work the same way
prompt1 = prompt_template1.invoke({"topic": "cats"})

print("Method 1 (tuples):", prompt1)

# Get response from model (using either prompt)
response = model.invoke(prompt1)
print("\nModel response:", response)
print("\nResponse content:", response.content)