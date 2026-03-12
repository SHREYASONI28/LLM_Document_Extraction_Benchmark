from fastapi import FastAPI, UploadFile, File, Form
import subprocess

app = FastAPI()


@app.get("/")
def home():
    return {"message": "LLM Document Extraction API Running"}


# -------- DOCUMENT EXTRACTION --------
@app.post("/extract")
async def extract_document(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):

    temp_file = f"temp_{file.filename}"

    # Save uploaded file
    with open(temp_file, "wb") as f:
        f.write(await file.read())

    # Run benchmark script
    subprocess.run([
        "python3",
        "benchmark.py",
        "--input",
        temp_file,
        "--prompt",
        prompt
    ])

    return {
        "status": "Benchmark completed"
    }


# -------- ACCURACY CALCULATION --------
@app.post("/accuracy")
def calculate_accuracy(prompt: str = Form(...)):

    subprocess.run([
        "python3",
        "accuracy.py",
        "--prompt",
        prompt
    ])

    return {
        "status": "Accuracy calculated",
        "output_file": "benchmark_accuracy.xlsx"
    }
