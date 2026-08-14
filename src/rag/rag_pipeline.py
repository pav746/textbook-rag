from .prompts import create_prompt
from .llm import get_ai_response


def answer_question(question, context):
    """
    Generates an answer to the user's question
    using relevant information from the textbook.

    question = user's question
    context = relevant textbook information
    """

    # Create a prompt using the question and textbook information
    prompt = create_prompt(question, context)

    # Send the prompt to the AI
    answer = get_ai_response(prompt)

    # Return the AI's answer
    return answer