from openai import OpenAI
import json

# Add your OpenAI API Key here
client = OpenAI(
    api_key="YOUR_API_KEY_HERE"
)

messages = [
    "My payment got deducted but service is not activated",
    "App crashes every time I login",
    "How to change my email address?"
]

def classify_message(message):
    prompt = f"""
You are a support ticket classifier.

Classify the given message into:

Categories:
- Billing
- Technical Issue
- Account
- General Inquiry

Priority Levels:
- High
- Medium
- Low

Return ONLY valid JSON:
{{
    "category": "",
    "priority": ""
}}

Message:
"{message}"
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    try:
        return json.loads(result)
    except:
        return {
            "category": "Unknown",
            "priority": "Unknown"
        }

final_output = []

for msg in messages:
    classified = classify_message(msg)

    final_output.append({
        "message": msg,
        "category": classified["category"],
        "priority": classified["priority"]
    })

print(json.dumps(final_output, indent=4))
