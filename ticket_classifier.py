import google.generativeai as genai
import json

# Add your Gemini API Key here
genai.configure(api_key="AIzaSyAI35wdPm8638Cs_1Ew0-XUoYi-cWycK8A")

model = genai.GenerativeModel("gemini-2.5-flash")

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

Return ONLY valid JSON like this:

{{
    "category": "",
    "priority": ""
}}

Message:
"{message}"
"""

    response = model.generate_content(prompt)

    result = response.text.strip()

    # Remove markdown if Gemini adds ```json
    result = result.replace("```json", "").replace("```", "").strip()

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
