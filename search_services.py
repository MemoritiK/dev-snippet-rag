from index_generation import *
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

def search_snippets(input_text, mode=1, top_k=TOP_K, difficulty="all"):
    """
    Search snippets by mode and optional difficulty.
    mode: 1=query, 2=code, 3=tags
    difficulty: 'easy', 'medium', 'hard', or 'all'
    """
    if mode == 1:
        index = index_query
    elif mode == 2:
        index = index_code
    elif mode == 3:
        index = index_tags
    else:
        raise ValueError("mode must be 1, 2, or 3")
    
    # Encode input
    q_emb = model.encode([input_text], convert_to_numpy=True)
    q_emb = q_emb / np.linalg.norm(q_emb)
    
    D, I = index.search(q_emb, top_k)
    
    results = []
    for idx, score in zip(I[0], D[0]):
        snippet = snippets[idx].copy()
        snippet["score"] = float(score)
        results.append(snippet)
    
    if difficulty != "all":
        results = [r for r in results if r.get("difficulty") == difficulty]
    
    return results


if __name__ == "__main__":    
    query_text = "create a barplot with pandas"
    results = search_snippets(query_text, mode=1, top_k=3)
    
    for r in results:
        print(f"Category: {r['category']}, Score: {r['score']:.3f}")
        print(f"Question: {r['question']}")
        print("Difficulty:", r["difficulty"])
        print("Code:\n", r['code'].replace("\\n", "\n"))
        print("-"*50,"\n")