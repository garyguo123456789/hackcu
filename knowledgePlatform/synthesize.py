import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async

load_dotenv()

async def main():
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
        input="""You are an agent responsible for synthesizing useful 
        class information insights. 
       
        
        Based on given information, summarize in bullet points useful knoweldge, e.g. this class is easy, that class is a torture""",
        model="openai/gpt-4.1",
        mcp_servers=[
        ]
    )

    print(f"Results:\n{result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())