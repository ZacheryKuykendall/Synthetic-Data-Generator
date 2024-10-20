# Synthetic Dataset Generator 🚀📝



This repository provides a Python script that uses a large language model (LLM) to generate synthetic data, tailored for educational and research purposes across various domains like bioinformatics, finance, education, or specialized subjects such as genomics. The dataset generation pipeline aims to simulate realistic queries and responses, ideal for training machine learning models, educational content, or prototype testing.

---

## About 🧪

The Synthetic Dataset Generator is designed to create synthetic datasets that mirror real-world scenarios, such as generating training data for machine learning models, creating educational content, or prototyping new applications in areas like finance, education, and genomics. By leveraging the **nvidia/Mistral-NeMo-Minitron-8B-Instruct** model from Hugging Face, the script can generate data suitable for researchers, educators, and machine learning enthusiasts. The generator allows for easy customization, making it suitable for various levels of expertise in any field of interest.

---

## Features (In-Depth) ✨

### 🔍 Large Language Model (LLM) Integration

Uses **nvidia/Mistral-NeMo-Minitron-8B-Instruct** from Hugging Face to provide advanced text generation, resulting in high-quality data that can be tailored to multiple domains such as bioinformatics, finance, and education. This model offers robust and contextually relevant responses, making it ideal for generating synthetic data for various applications.

### 🧠 Gradient Checkpointing

Implements gradient checkpointing to minimize GPU memory usage during the text generation process, making it possible to use larger models even with limited hardware resources. This allows users to perform efficient model inference without running into memory issues, especially on GPUs with smaller memory capacities.

### 📊 Batch Processing

Efficiently processes and writes dataset rows to CSV files in batches, reducing the overhead associated with file I/O operations and improving overall performance. Batch processing helps in handling large datasets seamlessly, making the data generation process faster and more resource-efficient.

### ⚙️ Environment Variables Customization

Allows easy customization of model parameters, cache directories, and other settings through a `.env` file, offering flexibility in how the script is run. Users can easily change model names, output file paths, and other configurations without modifying the core script, ensuring adaptability for different projects.

### 📝 Customizable Prompt Templates

The prompt templates used to generate the dataset can be easily customized to suit different domains such as finance, education, or genomics, allowing the generator to adapt to a wide range of applications. Users can modify the prompts to generate more domain-specific responses, providing better relevance for specialized use cases.

### 🌍 Multi-Domain Flexibility

The script can generate synthetic data for a variety of domains. This flexibility makes it suitable for applications in finance, education, healthcare, and more, based on user customization of prompts and contexts. Whether it's creating educational content or generating financial insights, the script can be tailored to meet specific needs.

### ⚡ Command Line Integration

Users can pass environment variables directly via the command line to override `.env` settings, making it easy to adapt configurations without editing the file. This feature is ideal for quick testing, deployment, or running multiple configurations in different environments without making persistent changes to the codebase.

### 💾 CPU Offloading Support

Supports CPU offloading to manage memory usage effectively when GPU resources are limited. This feature allows users to offload parts of the model or its computations to the CPU, enabling the use of large models on systems with constrained GPU memory.

### 🔄 Retry Mechanism for API Calls

Implements a retry mechanism using the `backoff` library to handle transient errors during model loading or data generation. This ensures that the script can recover from temporary issues, providing a more reliable data generation process.

### 🧠 Gradient Checkpointing

Implements gradient checkpointing to minimize GPU memory usage during the text generation process, making it possible to use larger models even with limited hardware resources.

### 📊 Batch Processing

Efficiently processes and writes dataset rows to CSV files in batches, reducing the overhead associated with file I/O operations and improving overall performance.

### ⚙️ Environment Variables Customization

Allows easy customization of model parameters, cache directories, and other settings through a `.env` file, offering flexibility in how the script is run.

### 📝 Customizable Prompt Templates

The prompt templates used to generate the dataset can be easily customized to suit different domains such as finance, education, or genomics, allowing the generator to adapt to a wide range of applications.

### 🌍 Multi-Domain Flexibility

The script can generate synthetic data for a variety of domains. This flexibility makes it suitable for applications in finance, education, healthcare, and more, based on user customization of prompts and contexts.

### ⚡ Command Line Integration

Users can pass environment variables directly via the command line to override `.env` settings, making it easy to adapt configurations without editing the file, ideal for quick testing and deployment.

---

### Environment Variables 🌱

The script uses a `.env` file to manage configurations:

- **`.env`**\*\* File\*\*: Contains default settings for the model name, cache directory, number of rows to generate, and output file name.
  - Example `.env` file:
- **Alternative Methods**: You can also pass environment variables directly in the command line before running the script:

---

### Customizing Prompts for Different Subjects ✨

The script can be easily customized to generate data for different subjects, such as finance, education, or genomics. Here’s how you can modify it:

1. **Edit Prompt Templates**: Locate the part of the script where the system prompt and user prompt are defined (usually in the `generate_prompt()` function). Update these prompts to reflect the subject area you want to generate data for.
   - For example, change "You are an expert in bioinformatics..." to "You are an expert in finance..." for generating finance-related datasets. Locate the part of the script where the system prompt and user prompt are defined. Update these prompts to reflect the subject area you want to generate data for.
   - For example, change `"You are an expert in bioinformatics..."` to `"You are an expert in finance..."` for generating finance-related datasets.
2. **Modify Context and Columns**: Update the context generation and column names to suit the specific subject you are targeting. For instance, in the CSV file, replace columns like `suggested_tools_software` with more appropriate categories such as `financial_metrics` or `educational_resources`.
3. **Update ********************`.env`******************** File**: Modify the `.env` file to use different models if needed, or adjust the number of rows and output file names based on your requirements.

---

## Getting Started 🚀

### Clone the Repository 🖥️

First, clone the repository:
```
git clone https://github.com/ZacheryKuykendall/Synthetic-Data-Generator.git
```

This repository contains a Python script for generating synthetic datasets using a large language model. Inside, you will find the necessary scripts, a sample `.env` configuration file, and instructions to help you set up and run the generator effectively.

### Set Up Virtual Environment 🐍

For Linux/macOS:
```
python -m venv venv
venv/Scripts/activate
```
For Windows:
```
python3 -m venv venv
source venv/bin/activate
```
### Install Dependencies 📦

Install the required dependencies:
```
pip install -r requirements.txt
```

---

## Step by Step Guide 📋

### Setting Up in Visual Studio Code 💻

1. **Clone the Repository**: Open Visual Studio Code and clone the repository by selecting **View > Command Palette** and typing `Git: Clone`.
2. **Open the Folder**: Navigate to the cloned directory in VS Code.
3. **Set Up Virtual Environment**:
   - Open the integrated terminal (**View > Terminal**).
   - Run the following commands to create and activate a virtual environment:
4. **Install Dependencies**: Run:
5. **Run the Script**: You can run the script directly in the VS Code terminal:
6. **Using the ********************`.env`******************** File**: Create a `.env` file in the root of the project and add the necessary environment variables to configure your run.

---

### Setting Up via Command Line (Linux) 🐧

1. **Clone the Repository**:
```
git clone https://github.com/ZacheryKuykendall/Synthetic-Data-Generator.git
```
2. **Set Up Virtual Environment**:
```
python -m venv venv
source venv/bin/activate
```
3. **Install Dependencies**:
```
pip install -r requirements.txt
```
4. **Run the Script**:
```
python generate.py
```
---

### Setting Up via Command Line (Windows) 🪟

1. **Clone the Repository**:
```
git clone https://github.com/ZacheryKuykendall/Synthetic-Data-Generator.git
```
2. **Set Up Virtual Environment**:
```
python3 -m venv venv
venv/Scripts/activate
```
3. **Install Dependencies**:
```
pip install -r requirements.txt
```
4. **Run the Script**:
```
python generate.py
```
---

## Usage ⚡

To generate the dataset, simply run:
```
python generate.py
```

This will load the specified model from Hugging Face and generate synthetic data according to your configuration.

### Parameters 🔧

- **HUGGINGFACE\_MODEL**: The name of the model to use for text generation.
- **HF\_CACHE\_DIR**: Directory for caching model files.
- **NUM\_ROWS**: The number of rows to generate.
- **OUTPUT\_FILE**: The output CSV file for storing the generated dataset.

---

## Output 📄

The generated dataset will be saved as a CSV file with the following customizable columns (users can add, remove, or rename columns based on their specific use case):

- **system\_prompt**: Describes the role and purpose of the AI model.
- **user\_experience\_level**: The user's knowledge level (e.g., beginner, intermediate, advanced).
- **context**: Context about the user's project and specific needs.
- **user\_prompt**: The user's specific question or request.
- **completion**: The generated response by the model.
- **customizable\_columns**: Add or modify columns based on your subject (e.g., `financial_metrics`, `educational_resources`).

---

## Example 🎓

Below is an example of a user prompt and the model's generated response:

- **User Prompt**: "What are the key factors in financial risk assessment?"
- **Generated Response**: "Key factors in financial risk assessment include market volatility, credit risk, liquidity, and regulatory compliance."

---

## Contributing 🤝

Contributions are welcome! Please open an issue to discuss any changes or improvements.

---

## License 📜

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contact 📧

For more information, feel free to reach out at [[zachery@the-node.co](mailto\:zachery@the-node.co)].

