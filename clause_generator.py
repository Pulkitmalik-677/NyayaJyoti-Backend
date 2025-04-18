import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import util

def find_best_match_semantic(user_input, embedder, instruction_embeddings, df):
    user_embedding = embedder.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(user_embedding, instruction_embeddings)[0]
    best_idx = torch.argmax(cosine_scores).item()
    best_score = cosine_scores[best_idx].item()
    if best_score > 0.4:
        return df.iloc[best_idx]
    return None

def build_prompt(example_1, example_2, instruction):
    return (
        "You are a legal assistant specialized in drafting formal legal clauses.\n"
        f"Example 1:\nClause: {example_1}\nEndClause\n\n"
        f"Example 2:\nClause: {example_2}\nEndClause\n\n"
        f"Now, generate ONLY the legal clause for {instruction}, using formal legal language.\n"
        "Output only the text between the markers 'Clause:' and 'EndClause'.\n\nClause: "
    )

def generate_clause(prompt_text, tokenizer, model, device):
    input_ids = tokenizer.encode(prompt_text, return_tensors="pt").to(device)
    output_ids = model.generate(
        input_ids,
        max_length=300,
        temperature=0.35,
        top_k=50,
        top_p=0.85,
        repetition_penalty=1.2,
        do_sample=True,
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id
    )
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    if "EndClause" in generated_text:
        return generated_text.split("Clause:")[1].split("EndClause")[0].strip()
    return generated_text.split("Clause:")[1].strip()

def fill_parameters_dynamic(clause_text, param_string):
    placeholders = set(re.findall(r"{(.*?)}", clause_text))
    defined_params = [p.strip() for p in str(param_string).split(',') if p.strip()]
    combined_params = sorted(placeholders.union(set(defined_params)))
    param_values = {}
    for param in combined_params:
        value = f"[{param}]"  # Placeholder since we can't interact in web
        param_values[param] = value
    for param, value in param_values.items():
        clause_text = clause_text.replace(f"{{{param}}}", value)
    return clause_text, param_values
