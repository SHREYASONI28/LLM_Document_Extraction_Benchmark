# 🚀 LLM Document Extraction Benchmark


# 📖 Overview

This project provides a **benchmarking framework to evaluate Large Language Models (LLMs)** for **structured information extraction from documents**.

The system extracts structured information from documents using multiple LLMs and compares their performance based on:

- ⚡ **Execution Time**
- 🎯 **Extraction Accuracy**
- 📊 **Precision, Recall, and F1 Score**

The results are automatically generated in **Excel reports**, making it easy to compare model performance.

The project also includes a **FastAPI API** that allows document extraction and benchmarking through **Swagger UI**.



# 🎯 Project Goal

The goal of this project is to build a **generic and configurable benchmarking framework** for evaluating how effectively **LLMs extract structured information from real-world documents**.

This framework helps determine:

- 🧠 **Most accurate model**
- ⚡ **Fastest model**
- 📄 **Best model for document information extraction systems**

The system is **configuration-driven**, meaning new extraction tasks can be added without modifying the main code.



# 🧠 Models Evaluated

The system benchmarks both **local LLMs (Ollama)** and **cloud LLMs (Azure OpenAI)**.

| Model | Platform | Description |
|------|------|-------------|
| **Llama3 (8B)** | Ollama | Open-source LLM by Meta |
| **Mistral (7B)** | Ollama | Lightweight high-performance LLM |
| **Qwen2.5 (7B)** | Ollama | Advanced LLM developed by Alibaba |
| **GPT-4.1** | Azure OpenAI | High accuracy cloud LLM |
| **Azure Llama 3.1 (8B)** | Azure AI | Hosted Llama model on Azure |

Each model processes the **same document and extraction prompt** to ensure fair comparison.



# 🏗️ System Architecture

```
Document (PDF / TXT / DOCX / XLSX)
            ↓
      Text Extraction
            ↓
   Prompt + JSON Template
            ↓
      LLM Processing
   (Ollama + Azure LLMs)
            ↓
     Structured JSON Output
            ↓
   Benchmark Excel Report
            ↓
     Accuracy Evaluation
            ↓
   Final Accuracy Report
```


# 📂 Project Structure

```
LLM_Document_Extraction_Benchmark/

├── config/
│   ├── invoice_config.json
│   └── resume_config.json
│
├── documents/
│   ├── invoices/
│   └── resumes/
│
├── benchmark.py
├── accuracy.py
├── app.py
│
├── benchmark_output.xlsx
├── benchmark_accuracy.xlsx
│
├── README.md
├── .env
└── venv/
```



# 📄 Supported Document Formats

The system supports multiple document formats:

| Format | Description |
|------|-------------|
| **PDF** | Extracted using PyPDF |
| **TXT** | Direct text extraction |
| **DOCX** | Extracted using python-docx |
| **XLSX** | Extracted using openpyxl |



# 📑 Supported Extraction Tasks

The system supports multiple information extraction tasks through **JSON configuration files**.

## Invoice Information Extraction

Example fields:

- Invoice Number  
- Invoice Date  
- Customer Name  
- Customer Email  
- Total Amount  

---

## Resume Information Extraction

Example fields:

- Name  
- Email  
- Phone  
- Skills  
- Education  
- Experience  
- Location  



# ⚙️ Configuration System

Extraction prompts and fields are defined using **JSON configuration files**.

Example structure:

```
config/
├── invoice_config.json
└── resume_config.json
```

### Example Configuration

```json
{
  "prompt": "Extract name, email, phone, skills, education, experience and location from the document.",
  "fields": [
    "name",
    "email",
    "phone",
    "skills",
    "education",
    "experience",
    "location"
  ]
}
```

This allows the framework to support **different extraction tasks without modifying the code**.



# ⚡ Execution Time Benchmark

The system records the **execution time of each model**.

Example:

| Model | Execution Time |
|------|----------------|
| Llama | 58.24 sec |
| Mistral | 89.71 sec |
| Qwen | 62.28 sec |
| GPT-4.1 | 4.12 sec |
| Azure Llama | 1.99 sec |

This helps identify **the fastest model for document processing**.



# 🎯 Accuracy Evaluation

Predictions are compared with **Ground Truth values** to evaluate model performance.

Metrics calculated:

- Accuracy
- Precision
- Recall
- F1 Score

Matching is calculated using:

```
difflib.SequenceMatcher
```

Additional validation includes:

- Text normalization
- Substring matching
- Similarity threshold comparison



# 📊 Benchmark Output

Running the benchmark generates:

```
benchmark_output.xlsx
```

Each sheet contains:

- Extracted fields
- Ground truth values
- Predictions from each model
- Model execution time

Example:

| Field | Ground Truth | Llama | Mistral | Qwen | GPT-4.1 | Azure-Llama |
|------|------|------|------|------|------|------|
| Name | Arjun Kapoor | Arjun Kapoor | Arjun Kapoor | Arjun Kapoor | Arjun Kapoor | Arjun Kapoor |

---

# 📊 Accuracy Report

Running the accuracy script generates:

```
benchmark_accuracy.xlsx
```

Example summary:

| Document | Metric | Llama | Mistral | Qwen | GPT-4.1 | Azure-Llama |
|------|------|------|------|------|------|------|
| resume_experienced | Accuracy | 85.71 | 71.43 | 100 | 100 | 85.71 |
| | Precision | 85.71 | 71.43 | 100 | 100 | 85.71 |
| | Recall | 100 | 100 | 100 | 100 | 100 |
| | F1 Score | 92.31 | 83.33 | 100 | 100 | 92.31 |



# 🌐 FastAPI API

The project provides a **FastAPI API interface** for running document extraction and accuracy evaluation.

---

# 🚀 Run the API Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```



# 📑 Swagger UI

FastAPI automatically generates API documentation.

Open:

```
http://127.0.0.1:8000/docs
```

You can test endpoints directly using Swagger UI.



# 📂 API Endpoints

## GET /

Check API status.

Example response:

```json
{
  "message": "LLM Document Extraction API Running"
}
```

---

## POST /extract

Runs the **benchmark pipeline**.

Parameters:

| Parameter | Description |
|------|-------------|
| file | Document file |
| config | Path to config JSON |
| prompt | Custom extraction prompt |

Example:

```
config/resume_config.json
```

This generates:

```
benchmark_output.xlsx
```

---

## POST /accuracy

Calculates extraction accuracy.

Parameters:

| Parameter | Description |
|------|-------------|
| config | Config file |
| prompt | Custom prompt |

Output:

```
benchmark_accuracy.xlsx
```

Example response:

```json
{
  "status": "Accuracy calculated",
  "output_file": "benchmark_accuracy.xlsx"
}
```



# ⚡ Quick Start

## 1️⃣ Install Dependencies

```bash
pip install pandas pypdf python-docx openpyxl python-dotenv openai fastapi uvicorn
```

---

## 2️⃣ Configure Azure

Create `.env` file:

```
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint

AZURE_API_VERSION_GPT=2024-02-15-preview
AZURE_API_VERSION_LLAMA=2024-02-15-preview
```

---

## 3️⃣ Run Benchmark

Example:

```bash
python benchmark.py \
--input documents/resumes/sample_resume.pdf \
--config config/resume_config.json
```

Output:

```
benchmark_output.xlsx
```

---

## 4️⃣ Run Accuracy Evaluation

```bash
python accuracy.py --config config/resume_config.json
```

Output:

```
benchmark_accuracy.xlsx
```

# ✨ Key Features

- Multi-model LLM benchmarking  
- Supports **PDF, TXT, DOCX, XLSX documents**  
- Configurable extraction prompts  
- Multiple document extraction tasks  
- Structured JSON extraction  
- Execution time benchmarking  
- Accuracy metrics (Precision, Recall, F1 Score)  
- Automated Excel report generation  
- FastAPI API interface  
- Swagger UI testing  

