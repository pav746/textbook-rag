def check_answer(answer, context):
    """
    Performs a simple check to see whether the answer
    contains information from the provided textbook context.

    answer = AI-generated answer
    context = relevant textbook information
    """

    if not answer:
        return {
            "supported": False,
            "message": "No answer was generated."
        }

    if not context:
        return {
            "supported": False,
            "message": "No textbook information was provided."
        }

    # Split the answer into words
    answer_words = set(answer.lower().split())

    # Split the textbook context into words
    context_words = set(context.lower().split())

    # Find words that appear in both
    common_words = answer_words.intersection(context_words)

    # Calculate a simple overlap score
    overlap_score = len(common_words) / max(len(answer_words), 1)

    if overlap_score >= 0.20:
        return {
            "supported": True,
            "score": round(overlap_score, 2),
            "message": "The answer appears to be supported by the textbook context."
        }

    return {
        "supported": False,
        "score": round(overlap_score, 2),
        "message": "The answer may not be sufficiently supported by the textbook context."
    }