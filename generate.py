import csv
import os
from dotenv import load_dotenv
import random
import backoff
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm
import pathlib

# Load environment variables from .env file
load_dotenv()

# Lazy-load model and tokenizer so that simply importing this module doesn't
# immediately trigger large downloads. They are initialized when
# ``generate_dataset`` is first called.
tokenizer = None
model = None
generator = None

def _load_model():
    """Load the Hugging Face model and tokenizer if needed."""
    global tokenizer, model, generator
    if generator is not None:
        return

    model_name = os.getenv("HUGGINGFACE_MODEL")
    cache_dir = pathlib.Path(os.getenv("HF_CACHE_DIR", "./model_cache"))

    print(
        f"Loading model '{model_name}' from Hugging Face... This may take a while if it's the first time."
    )

    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)
    except (OSError, ValueError):
        print(
            f"Model '{model_name}' not found locally. Downloading from Hugging Face..."
        )
        tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)

    model.gradient_checkpointing_enable()
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device_map="auto")

# Helper function to generate response from local Hugging Face model
@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def generate_response(system_prompt, user_prompt):
    try:
        input_text = f"{system_prompt}\n{user_prompt}"
        max_length = len(input_text.split()) + 100  # Dynamically adjust max_length based on input length
        response = generator(input_text, max_length=max_length, num_return_sequences=1, temperature=0.7, do_sample=True, truncation=True)
        return response[0]['generated_text'].replace(input_text, '').strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return ""

# Helper function to create dataset row
def create_dataset_row(system_prompt, experience_level, context, user_prompt, completion):
    suggested_tools = "BLAST, DESeq2, Ensembl" if "RNA-Seq" in user_prompt else "NCBI, KEGG, UniProt"
    cautions = "Consider data quality and normalization before analysis." if "analysis" in user_prompt else "Ensure ethical data sharing practices."
    response_type = "definition" if "What is" in user_prompt else "step-by-step instructions"
    data_source = "GEO database" if "RNA-Seq" in user_prompt else "KEGG pathway database"
    real_world_app = "Cancer biomarker identification" if "cancer" in user_prompt else "Protein function prediction"

    return {
        "system_prompt": system_prompt,
        "user_experience_level": experience_level,
        "context": context,
        "user_prompt": user_prompt,
        "completion": completion,
        "suggested_tools_software": suggested_tools,
        "cautions_and_considerations": cautions,
        "response_type": response_type,
        "data_source_or_method": data_source,
        "real_world_application": real_world_app
    }


def generate_dataset(num_rows: int = 200, output_file: str = "synthetic_bioinformatics_dataset.csv") -> str:
    """Generate a synthetic dataset and save it to ``output_file``."""
    _load_model()

    system_prompt = (
        "You are a specialist in computational biology and bioinformatics. "
        "Your purpose is to assist users in understanding and applying computational methods and tools to analyze "
        "and interpret biological data, including genomics, transcriptomics, and proteomics. Provide clear explanations "
        "of complex concepts, offer guidance on data analysis and interpretation, and suggest best practices for integrating "
        "computational approaches into biological research and applications."
    )

    experience_levels = ["beginner", "intermediate", "advanced"]
    user_prompts = [
        "What is the difference between DNA sequencing and RNA sequencing?",
        "How do I perform a differential gene expression analysis using RNA-Seq data?",
        "What are the best practices for assembling a transcriptome?",
        "Can you explain how to use BLAST for sequence alignment?",
        "What considerations should I keep in mind when analyzing single-cell RNA-Seq data?",
        "How do I integrate genomics and proteomics data for pathway analysis?",
        "What are common tools for protein structure prediction?",
        "How do I identify differentially expressed genes related to cancer?",
    ]

    COLUMNS = [
        "system_prompt",
        "user_experience_level",
        "context",
        "user_prompt",
        "completion",
        "suggested_tools_software",
        "cautions_and_considerations",
        "response_type",
        "data_source_or_method",
        "real_world_application",
    ]

    dataset = []
    BATCH_SIZE = 50

    with tqdm(total=num_rows, desc="Generating dataset rows", unit="row") as pbar:
        for i in range(num_rows):
            experience_level = random.choice(experience_levels)
            user_prompt = random.sample(user_prompts, 1)[0]
            project_types = [
                "genomics research",
                "transcriptomics study",
                "proteomics analysis",
                "cancer biomarker discovery",
                "metagenomics project",
                "single-cell analysis",
                "epigenetics research",
                "disease pathway modeling",
            ]
            project_type = random.choice(project_types)
            context = f"User is working on a {project_type} and needs detailed guidance on {user_prompt.lower()}"

            completion = generate_response(system_prompt, user_prompt)
            if not completion.strip():
                pbar.update(1)
                continue

            row = create_dataset_row(system_prompt, experience_level, context, user_prompt, completion)
            dataset.append(row)

            if len(dataset) >= BATCH_SIZE:
                with open(output_file, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=COLUMNS)
                    if i < BATCH_SIZE:
                        writer.writeheader()
                    writer.writerows(dataset)
                dataset = []

            pbar.update(1)

    if dataset:
        with open(output_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=COLUMNS)
            if num_rows <= BATCH_SIZE:
                writer.writeheader()
            writer.writerows(dataset)

    print(f"Dataset successfully generated and saved to {output_file}")
    return output_file


if __name__ == "__main__":
    num_rows = int(os.getenv("NUM_ROWS", 200))
    output_file = os.getenv("OUTPUT_FILE", "synthetic_bioinformatics_dataset.csv")
    generate_dataset(num_rows=num_rows, output_file=output_file)

