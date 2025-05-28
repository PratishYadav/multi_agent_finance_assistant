from openai import OpenAI

def generate_summary(risk_info, earnings_info, sentiment="neutral"):
    prompt = f"""
    Risk Info: {risk_info}
    Earnings: {earnings_info}
    Sentiment: {sentiment}
    
    Give me a 2-3 sentence brief on Asia tech market today.
    """
    # Call LLM API (OpenAI or HuggingFace)
    return "Today, your Asia tech allocation is 22%, ..."

