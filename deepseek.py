# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

#I used this 1.5B parameter model, due to hardware limitations. This model is inefficient for actual projects.
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")

def generate_response(prompt: str) -> str:
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    
    # Create an attention mask
    attention_mask = inputs["attention_mask"] if "attention_mask" in inputs else None
    
    # Generate a response
    outputs = model.generate(
        inputs["input_ids"], 
        max_length=300, 
        num_return_sequences=1,
        attention_mask=attention_mask,  # pass the attention mask explicitly, else you might get warnings
        pad_token_id=tokenizer.eos_token_id  # use eos_token_id as pad_token_id if not set
    )
    
    # Decode the generated tokens to a string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response