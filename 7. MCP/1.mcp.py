from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
import time
from dotenv import load_dotenv
load_dotenv()
import os
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams

async def main():
    
    params = StdioServerParams(
        command = 'uvx',
        args=['mcp-server-time','--local-timezone=America/New_York']
    )
    
    model = OpenAIChatCompletionClient(model='gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))
    
    
    async with McpWorkbench(server_params=params) as workbench:
        agent = AssistantAgent(
            name = 'Agent',
            system_message='You are a helpful assistant',
            model_client = model,
            workbench=workbench,
            reflect_on_tool_use=True
        )
        
        
        task = 'What is the current time right now in Kelowna'
        
        async for message in agent.run_stream(task=task):
            print("-"*100)
            print(message)
            print('-'*100)
            
if __name__ == '__main__':
    asyncio.run(main())