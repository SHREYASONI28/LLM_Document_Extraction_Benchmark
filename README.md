# 🚀 LLM Document Extraction Benchmark

## 📖 Overview

This project provides a **benchmarking framework for evaluating Large Language Models (LLMs)** on **structured information extraction from documents**.

The system extracts structured information from documents using multiple LLMs and compares their performance based on:

- ⚡ **Execution Time**
- 🎯 **Extraction Accuracy**
- 📊 **Precision, Recall, and F1 Score**

Results are automatically generated in **Excel reports**, making it easy to compare model performance.

The project also includes a **FastAPI API** that allows document extraction and benchmarking through **Swagger UI**.



# 🎯 Project Goal

The goal of this project is to build a **generic benchmarking framework** for evaluating how effectively **LLMs extract structured information from real-world documents**.

This framework helps determine:

- 🧠 **Most accurate model**
- ⚡ **Fastest model**
- 📄 **Best model for document information extraction systems**

The system supports **prompt-based extraction**, allowing users to define extraction fields dynamically.



# 🧠 Models Evaluated

The system benchmarks both **local LLMs (Ollama)** and **cloud LLMs (Azure OpenAI)**.

| Model | Platform | Description |
|------|------|-------------|
| **Llama3 (8B)** | Ollama | Open-source LLM by Meta |
| **Mistral (7B)** | Ollama | Lightweight high-performance LLM |
| **Qwen2.5 (7B)** | Ollama | Advanced LLM developed by Alibaba |
| **GPT-4.1** | Azure OpenAI | High-accuracy cloud LLM |
| **Azure Llama 3.1 (8B)** | Azure AI | Hosted Llama model on Azure |

Each model processes the **same document and extraction prompt** to ensure fair comparison.



# 🏗️ System Architecture

```
Document (PDF / TXT / DOCX / XLSX)
            ↓
      Text Extraction
            ↓
      Extraction Prompt
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

├── benchmark.py
├── accuracy.py
├── app.py
│
├── benchmark_output.xlsx
├── benchmark_accuracy.xlsx
│
├── README.md
├── .gitignore
└── .env
```

# 📄 Supported Document Formats

The system supports multiple document formats:

| Format | Description |
|------|-------------|
| **PDF** | Extracted using PyPDF |
| **TXT** | Direct text extraction |
| **DOCX** | Extracted using python-docx |
| **XLSX** | Extracted using openpyxl |

---

# 🧾 Extraction Method

Information extraction is controlled using **prompts**.

Example prompt:

```
Extract name, email, phone, skills, education, and experience from the document.
```

Fields are automatically extracted from the prompt and used to generate structured JSON output.



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

This helps identify the **fastest model for document processing**.



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
|---------|--------|------|--------|------|--------|-------------|
| temp_resume_experienced | Accuracy | 100 | 71.43 | 85.71 | 100 | 85.71 |
|  | Precision | 100 | 71.43 | 85.71 | 100 | 85.71 |
|  | Recall | 100 | 100 | 100 | 100 | 100 |
|  | F1 Score | 100 | 83.33 | 92.31 | 100 | 92.31 |



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

---

# 📂 API Endpoints

## GET /

Check API status.

Example response:

```json
{
  "message": "LLM Document Extraction API Running"
}
```



## POST /extract

Runs the **benchmark pipeline**.

Parameters:

| Parameter | Description |
|------|-------------|
| file | Document file |
| prompt | Extraction prompt |

Example prompt:

```
Extract name, email, phone, skills
```

This generates:

```
benchmark_output.xlsx
```



## POST /accuracy

Calculates extraction accuracy.

Parameters:

| Parameter | Description |
|------|-------------|
| prompt | Extraction prompt |

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

```bash
python benchmark.py \
--input sample_resume.pdf \
--prompt "Extract name, email, phone, skills"
```

Output:

```
benchmark_output.xlsx
```



## 4️⃣ Run Accuracy Evaluation

```bash
python accuracy.py \
--prompt "Extract name, email, phone, skills"
```

Output:

```
benchmark_accuracy.xlsx
```



# 🌿 Repository Branches

| Branch | Description |
|------|-------------|
| **main** | Prompt-based extraction system |
| **with-config** | Configuration-based extraction version |



# ✨ Key Features

- Multi-model LLM benchmarking  
- Supports **PDF, TXT, DOCX, XLSX documents**  
- Prompt-driven extraction  
- Structured JSON extraction  
- Execution time benchmarking  
- Accuracy metrics (Precision, Recall, F1 Score)  
- Automated Excel report generation  
- FastAPI API interface  
- Swagger UI testing
