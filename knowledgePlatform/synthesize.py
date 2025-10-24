import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async

load_dotenv()

async def main():
    with open("knowledgeData.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
    
    # Convert JSON to a nicely formatted string
    json_str = json.dumps(json_data, indent=2, ensure_ascii=False)

    client = AsyncDedalus()
    runner = DedalusRunner(client)

    base_prompt = """You are an agent responsible for synthesizing useful 
    class information insights. 
    
    Based on given information, summarize in bullet points useful knowledge,
    e.g. this class is easy, that class is a torture.
    """

    llm_input = f"{base_prompt}\n\nHere is the provided data:\n{json_str}"

    result = await runner.run(
       input = llm_input,
        model="openai/gpt-4.1",
        mcp_servers=[
        ]
    )

    print(f"Results:\n{result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())