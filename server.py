import asyncio
from fastmcp import FastMCP

mcp = FastMCP(name="CloudYeller")

@mcp.tool()
async def yell_at_the_clouds(message: str) -> str:
    """
    Yell at the clouds after a delay proportional to string length.
    """
    # Calculate total wait time: 0.5s per char, capped at 30s
    wait = min(0.5 * len(message), 30.0)
    await asyncio.sleep(wait)
    return f"your string {message} has been yelled at the clouds.  The clouds do not respond."

if __name__ == "__main__":
    mcp.run()  # Uses default STDIO transport
