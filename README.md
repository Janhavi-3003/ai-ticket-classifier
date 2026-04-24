# AI Support Ticket Classifier

## Project Overview

This project is used to classify customer support messages automatically using AI.

It helps customer support teams by reducing manual work and giving faster responses.

The system reads customer messages, finds the correct category, and assigns a priority level based on the issue.

---

## Features

* Accepts customer support messages
* Classifies messages into:

  * Billing
  * Technical Issue
  * Account
  * General Inquiry
* Assigns priority levels:

  * High
  * Medium
  * Low
* Gives output in JSON format
* Uses Gemini AI API for classification

---

## Technologies Used

* Python
* Gemini AI API
* JSON

---

## Input Example

```python
[
    "My payment got deducted but service is not activated",
    "App crashes every time I login",
    "How to change my email address?"
]
```

---

## Output Example

```json
[
    {
        "message": "My payment got deducted but service is not activated",
        "category": "Billing",
        "priority": "High"
    },
    {
        "message": "App crashes every time I login",
        "category": "Technical Issue",
        "priority": "High"
    },
    {
        "message": "How to change my email address?",
        "category": "Account",
        "priority": "Low"
    }
]
```

---

## Installation

First install the required package:

```bash
pip install google-generativeai
```

---

## How to Run

Run the Python file using:

```bash
python ticket_classifier.py
```

---

## Project Structure

```bash
ai-ticket-classifier/
│
├── ticket_classifier.py
├── README.md
├── output.png
```

---

## Approach

In this project, each customer message is sent to Gemini AI using a prompt.

The AI checks:

* what type of issue it is
* how urgent the issue is

Then it returns:

* category
* priority

Finally, the program stores the result in JSON format.

---

## Error Handling

If the AI gives an invalid response or JSON error happens, the program returns:

* category: Unknown
* priority: Unknown

This helps the program run safely without stopping.

---

## Author

Janhavi
