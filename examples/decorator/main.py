"""
Example MCP Agent application showing simplified agent access.
"""

import asyncio
from mcp_agent.core.decorator_app import FastAgent

# Create the application
agent_app = FastAgent("Interactive Agent Example")


# Define the agent
@agent_app.agent(
    name="foo",
    instruction="A simple agent that helps with basic tasks. Request Human Input when needed.",
    servers=["mcp_root"],
    #    model="gpt-4o", model override here takes precedence
)
async def main():
    # use the --model= command line switch to specify model
    async with agent_app.run() as agent:
        # await agent("print the next number in the sequence")
        # await agent.prompt(default="STOP")
        await agent.foo.send()


if __name__ == "__main__":
    asyncio.run(main())
