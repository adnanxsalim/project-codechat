import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(code_files, user_question):
    combined_code = ""
    for path, content in code_files:
        combined_code += f"\n# File: {path}\n{content}\n"

    # Truncate if too long for LLM context
    if len(combined_code) > 14000:
        combined_code = combined_code[:14000] + "\n...[truncated]..."

    prompt = f"""
You are an expert code reviewer.

Here is a codebase composed of the following files:
{combined_code}

Now, answer this question about the codebase:
\"{user_question}\"
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-4.1-mini",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error from LLM: {str(e)}"