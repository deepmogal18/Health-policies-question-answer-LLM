from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained("zai-org/GLM-4.5")
model = AutoModelForCausalLM.from_pretrained("zai-org/GLM-4.5")

def chat_with_glm(user_input: str, max_tokens: int = 100) -> str:
    messages = [
        {"role": "user", "content": user_input},
    ]
    
    # Tokenize using the chat template
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    # Generate output
    outputs = model.generate(**inputs, max_new_tokens=max_tokens)

    # Decode only the generated part
    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    return response.strip()
