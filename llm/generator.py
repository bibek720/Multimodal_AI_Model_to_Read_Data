import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(context, question):

    prompt = f"""
    You are a helpful assistant.

    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {question}

    If the answer is not in the context, say you don't know.
    """

    response = model.generate_content(prompt)

    return response.text