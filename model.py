from transformers import pipeline

# Load a pre-trained LLM like Codex for code analysis
review_pipeline = pipeline("text-generation", model="openai/code-davinci-002")

# Function to review the code using the LLM
def review_code(code):
    prompt = f"Review the following Python code for errors, security vulnerabilities, and best practices:\n\n{code}\n\n"
    response = review_pipeline(prompt, max_length=500, num_return_sequences=1)
    return response[0]['generated_text']
