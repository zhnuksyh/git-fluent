import argparse
import torch
from unsloth import FastLanguageModel

# --- CONFIGURATION ---
# We use the model you uploaded to Hugging Face
MODEL_NAME = "daimon-ml/gitfluent-llama3-8b"
MAX_SEQ_LENGTH = 2048
LOAD_IN_4BIT = True

def load_model():
    """Loads the model and tokenizer from Hugging Face."""
    print(f"⏳ Loading {MODEL_NAME}...")
    # This automatically handles downloading or loading from cache
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL_NAME,
        max_seq_length=MAX_SEQ_LENGTH,
        dtype=None,
        load_in_4bit=LOAD_IN_4BIT,
    )
    FastLanguageModel.for_inference(model)
    return model, tokenizer

def generate_git_command(prompt, model, tokenizer):
    """Generates a Git command based on the natural language prompt."""
    
    # Alpaca / Unsloth Instruction Format used during training
    alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
You are a Git expert. Convert the following natural language request into a Git command.

### Input:
{}

### Response:
"""
    
    inputs = tokenizer(
        [alpaca_prompt.format(prompt, "")], 
        return_tensors="pt"
    ).to("cuda")

    # Generate output
    outputs = model.generate(**inputs, max_new_tokens=64, use_cache=True)
    result = tokenizer.batch_decode(outputs)[0]
    
    # Clean extraction of just the command (removes the prompt text)
    command = result.split("### Response:")[-1].strip().replace("<|end_of_text|>", "")
    return command

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Gitfluent: Translate English to Git Commands")
    parser.add_argument("query", type=str, help="The natural language description (e.g., 'undo last commit')")
    args = parser.parse_args()

    try:
        model, tokenizer = load_model()
        print(f"🧠 Project Aidan is thinking about: '{args.query}'")
        
        command = generate_git_command(args.query, model, tokenizer)
        
        print("\n" + "="*40)
        print(f"Suggested Command:\n\033[1;32m{command}\033[0m") # Prints in Green
        print("="*40 + "\n")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
