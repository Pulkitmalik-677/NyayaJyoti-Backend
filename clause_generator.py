
from difflib import get_close_matches

def get_best_clause(prompt, df):
    prompt = prompt.lower()
    all_examples = df['example_1'].tolist() + df['example_2'].dropna().tolist()
    matches = get_close_matches(prompt, all_examples, n=1, cutoff=0.2)
    if matches:
        return matches[0]
    else:
        return "N/A"
