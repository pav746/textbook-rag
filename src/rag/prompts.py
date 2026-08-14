SYSTEM_PROMPT = """
You are a helpful textbook assistant.

Answer the user's question using only the information provided from the textbook.

If the answer cannot be found in the provided textbook information,
clearly say that the information is not available in the textbook.

Do not make up information.

Give clear and easy-to-understand answers.
"""


def create_prompt(question, context):
    """
    Creates the prompt that will be sent to the AI.

    question = what the user asked
    context = relevant information retrieved from the textbook
    """

    prompt = f"""
{SYSTEM_PROMPT}

Textbook information:
{context}

User question:
{question}

Answer the question using the textbook information above.
"""

    return prompt