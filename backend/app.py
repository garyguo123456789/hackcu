# backend/app.py
import asyncio
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow your frontend localhost:5173 etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    # Load your JSON data
    with open("data.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
    json_str = json.dumps(json_data, indent=2, ensure_ascii=False)

    # Build the prompt
    base_prompt = """You are an agent responsible for synthesizing useful class information insights.
    Based on given information, summarize in bullet points useful knowledge."""
    llm_input = f"{base_prompt}\n\nQuestion: {question}\n\nData:\n{json_str}"

    # Run Dedalus
    client = AsyncDedalus()
    runner = DedalusRunner(client)
    result = await runner.run(input=llm_input, model="openai/gpt-4.1")

    return {"answer": result.final_output}
