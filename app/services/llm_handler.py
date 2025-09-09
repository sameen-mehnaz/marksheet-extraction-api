import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Load API key from .env

def process_with_llm(raw_text):
    prompt = f"""
    Extract candidate details, subject-wise marks, overall result, and issue date from the following mark sheet text.
    Provide the output as strict JSON, including confidence scores (0-1).
    Text:
    {raw_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a structured data extraction expert."},
            {"role": "user", "content": prompt}
        ]
    )

    result = response['choices'][0]['message']['content']
    return result  # Should be valid JSON
