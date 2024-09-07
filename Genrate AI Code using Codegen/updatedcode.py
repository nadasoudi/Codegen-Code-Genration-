from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pandas as pd

# Load your CSV file
file_path = './Cleaned_ProblemSolutionPythonV3.csv'  # Assuming the CSV is in the same directory
df = pd.read_csv(file_path)

# Set the start and end row for this chunk
start_row =2501   # Change this for each chunk
end_row = 2800  # Change this for each chunk

# Select the chunk of data to process
df_chunk = df.iloc[start_row:end_row]

# Load the CodeGen model and tokenizer
model_name = "Salesforce/codegen-350M-mono"  # Choose the model size you prefer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Add a pad token if not present
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token  # Set pad_token to eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_code(problem_description):
    # Neutral prompt, without suggesting specific structures like functions
    prompt = f"Write Python code to solve the following problem:\n{problem_description}\n\nProvide the solution as Python code:"
    
    # Tokenize input and add attention mask
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    
    # Generate outputs with attention_mask
    outputs = model.generate(
        input_ids=inputs['input_ids'].to(model.device),
        attention_mask=inputs['attention_mask'].to(model.device),  # Add attention mask here
        max_length=150
    )
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract the code portion by splitting at the prompt end and taking the code part
    code_start = "Provide the solution as Python code:"
    generated_code = generated_text.split(code_start)[-1].strip()
    
    return generated_code

# Apply the code generation to each problem in the chunk
df_chunk['Generated_Code'] = df_chunk['Problem'].apply(generate_code)

# Save the results to a new CSV file
output_path = f'./generated_code2_{start_row}_{end_row}.csv'  # Save in the same directory
df_chunk.to_csv(output_path, index=False)

print(f"Processed rows {start_row} to {end_row}. Results saved to {output_path}")
