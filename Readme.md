# FAISS-Powered Data Analysis Snippets Search

This project provides a **semantic search engine for data analysis and visualization snippets** using **FAISS** and **sentence embeddings**. It allows you to quickly find relevant examples for **NumPy, Pandas, Matplotlib, Seaborn, and SciPy** tasks.


## Features

* **Semantic search:** Search by **natural language queries**, **data manipulation code**, or **tags**.
* **Fast vector search:** Powered by **FAISS**, enabling quick retrieval of relevant snippets.
* **Difficulty filtering:** Optional filter for snippet difficulty: `easy`, `medium`, or `hard`.
* **Embeddings:** Uses **SentenceTransformers** (`all-MiniLM-L6-v2`) to encode queries, snippet code, and tags.
* **Metadata storage:** Stores snippet metadata for fast lookup and offline use.


## Dataset

The project uses a **JSONL file (`cleaned_snippets.jsonl`)** containing data analysis snippets. Each snippet has the following structure:

```json
{
    "id": "unique-uuid",
    "category": "scatter-plot",
    "question": "How to create a scatter plot with Seaborn?",
    "code": "import seaborn as sns\nsns.scatterplot(data=df, x='x', y='y')",
    "difficulty": "easy",
    "tags": ["seaborn", "scatter", "visualization", "data-analysis"]
}
```

Includes examples for:

* **Data manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Scientific computation:** SciPy
* **Exploratory Data Analysis (EDA)** and plotting trends


## How it Works

1. **Build FAISS indices:** Separate indices are created for:

   * Natural language queries (`question`)
   * Code snippets (`code`)
   * Tags (`tags`)

2. **Search snippets:** The `search_snippets` function takes:

   * `input_text`: your query string
   * `mode`: 1 = query, 2 = code, 3 = tags
   * `top_k`: number of results to return
   * `difficulty`: optional filter (`easy`, `medium`, `hard`)

3. **Retrieve results:** Returns top matching snippets with scores, categories, and metadata.


## Usage Example

```python
from search_services import search_snippets

query_text = "create a barplot with pandas"
results = search_snippets(query_text, mode=1, top_k=3)

for r in results:
    print(f"Category: {r['category']}, Score: {r['score']:.3f}")
    print(f"Question: {r['question']}")
    print("Difficulty:", r["difficulty"])
    print("Code:\n", r['code'].replace("\\n", "\n"))
```
## results

```python
Category: bar-plot, Score: 0.739
Question: How to create a vertical bar chart with matplotlib?
Difficulty: easy
Code:
import matplotlib.pyplot as plt

labels = ['Q1', 'Q2', 'Q3', 'Q4']
values = [450, 520, 490, 600]

plt.bar(labels, values, color='skyblue', edgecolor='navy')
plt.title('Quarterly Revenue')
plt.ylabel('Revenue ($)')
plt.show()
--------------------------------------------------

Category: bar-plot, Score: 0.735
Question: How to create a stacked bar chart in Matplotlib?
Difficulty: medium
Code:
plt.bar(x, y1, label='Group A')
plt.bar(x, y2, bottom=y1, label='Group B')
plt.legend()
--------------------------------------------------

Category: barplot, Score: 0.687
Question: How to create a bar plot with seaborn?
Difficulty: easy
Code:
import seaborn as sns
import matplotlib.pyplot as plt

# Create toy data
data = {'Category': ['A', 'B', 'C', 'D'], 'Value': [10, 15, 7, 12]}
df = pd.DataFrame(data)

sns.barplot(x='Category', y='Value', data=df)
plt.title('Seaborn Bar Plot')
plt.show()
--------------------------------------------------
```

## Requirements

```text
faiss-cpu
sentence-transformers
numpy
torch
pickle
```

