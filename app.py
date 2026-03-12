from fastapi import FastAPI, UploadFile, File, Form
import subprocess
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LLM Document Extraction API Running"}

from typing import Optional
@app.post("/extract")


async def extract_document(
    file: UploadFile = File(...),
    config: Optional[str] = Form(None),
    prompt: Optional[str] = Form(None)
):

    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as f:
        f.write(await file.read())

    if config:
        subprocess.run([
            "python3",
            "benchmark.py",
            "--input",
            temp_file,
            "--config",
            config
        ])

    elif prompt:
        subprocess.run([
            "python3",
            "benchmark.py",
            "--input",
            temp_file,
            "--prompt",
            prompt
        ])

    else:
        return {"error": "Provide either config or prompt"}

    return {
         "status": "Benchmark completed"
    }


from typing import Optional

@app.post("/accuracy")
def calculate_accuracy(
    config: Optional[str] = Form(None),
    prompt: Optional[str] = Form(None)
):

    if config:
        subprocess.run([
            "python3",
            "accuracy.py",
            "--config",
            config
        ])

    elif prompt:
        subprocess.run([
            "python3",
            "accuracy.py",
            "--prompt",
            prompt
        ])

    else:
        return {"error": "Provide config or prompt"}

    return {
        "status": "Accuracy calculated",
        "output_file": "benchmark_accuracy.xlsx"
    }