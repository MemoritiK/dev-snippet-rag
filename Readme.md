# Dev Snippet RAG
A lightweight, IDE-adjacent code retrieval tool for Python data analysis developers who need **instant reference examples** when stuck mid-implementation.

This project focuses on **retrieving known working code patterns**, explaining them clearly, and optionally executing them to confirm intent — without breaking developer flow.


## Problem
When writing data analysis code, developers often:
- Remember *what* they want to do but not the exact syntax
- Get stuck mid-implementation
- Need a quick, reliable reference without searching the web
- Want to confirm behavior before copying code into their IDE

Traditional search engines and chatbots are slow, noisy, or opaque for this use case.


## Solution
Instant Code RAG provides:
- Semantic retrieval of curated Python data analysis snippets
- Grounded AI explanations strictly based on retrieved code
- Optional execution to verify behavior
- Minimal UI designed for quick reference, not conversation

This is **retrieval-augmented generation grounded in executable code**, not a general-purpose chatbot.

## Key Features

### Semantic Code Retrieval
- Search 800+ curated Python snippets using:
  - Natural language
  - Keywords
  - Partial or incomplete code
- Powered by FAISS vector search

### Grounded Explanations
- AI-generated explanations constrained to the retrieved snippet
- Focused on intent, usage, and key lines
- No hallucinated fixes or speculative code

### Optional Execution
- Execute snippets in a sandboxed environment
- View outputs or plots inline
- Used for **confirmation**, not exploration

### Metadata-Aware Results
Each snippet includes:
- Difficulty level
- Relevance score
- Category (NumPy, Pandas, Matplotlib, etc.)
- Associated intent question

### Copy-to-Clipboard
- One-click copy for immediate reuse in your IDE

## Intended Workflow

1. You are writing data analysis code in an IDE
2. You get stuck or forget a pattern
3. You open Instant Code RAG
4. You:
   - Describe what you want to do **or**
   - Paste partial / incorrect code
5. The system retrieves the closest known working pattern
6. You read a short explanation to confirm intent
7. Optionally execute to verify output
8. Copy and return to your IDE

## How It Works

1. **Search**:
   Enter a query → frontend sends a POST request to `/search`.

2. **Retrieve**:
   Backend searches preprocessed snippets using FAISS → returns top matches.

3. **Display**:
   Frontend shows snippet code, category, and associated question.

4. **Explain**:
   Click “Explain” → frontend calls `/explain` → AI explanation displayed inline.

5. **Copy**:
   Click “Copy” → snippet code copied to clipboard.

6. **Execution**:
   Click “Run” → backend executes code safely → output or plots shown inline.

## Live Demo

* **Frontend:** [https://faiss-data-analysis-snippets-9qgw4qsfc5jviqqkckwikv.streamlit.app/](https://faiss-data-analysis-snippets-9qgw4qsfc5jviqqkckwikv.streamlit.app/)
* **Backend API:** [https://faiss-data-analysis-snippets.onrender.com](https://faiss-data-analysis-snippets.onrender.com)

## Tech Stack

* **Backend:** Python, Flask, FAISS, NumPy, pickle, ONNX Runtime
* **Frontend:** Streamlit
* **AI:** kwaipilot/kat-coder-pro:free from OpenRouter

## Installation

```bash
git clone <repo_url>
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Start the Flask backend from /backend:

```bash
python app.py
```

2. Start the Streamlit frontend:

```bash
streamlit run frontend.py
```

3. Open the browser at the Streamlit URL and start searching code snippets.

## Environment Variables

Set your API key for the LLM:

```bash
export API_KEY="your_api_key_here"
```

In your requests:

```python
headers = {"Authorization": f"Bearer {API_KEY}"}
```

## Requirements

```text
Flask
flask-cors
numpy
pandas
matplotlib
seaborn
scipy
faiss-cpu
requests
pyyaml
tqdm
onnxruntime
statistics
random
pathlib
json
```
## Results
<img width="560" height="907" alt="image" src="https://github.com/user-attachments/assets/3257e1bf-1d55-475b-baa7-6cd03281f8c0" />
<img width="537" height="908" alt="image" src="https://github.com/user-attachments/assets/0a7996d2-187f-4a37-bdc0-8b8e92049622" />
<img width="583" height="910" alt="image" src="https://github.com/user-attachments/assets/a3bda74f-09b5-4fe5-8b72-31dd48b3f234" />

