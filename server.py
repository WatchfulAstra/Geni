from mcp.server.fastmcp import FastMCP
from browser import browser

mcp = FastMCP("Browser MCP")


@mcp.tool()
async def open_page(url: str) -> str:
    """Open a URL in the browser."""
    return await browser.open(url)


@mcp.tool()
async def click(selector: str) -> str:
    """Click an element using a CSS selector."""
    return await browser.click(selector)


@mcp.tool()
async def type_text(selector: str, text: str) -> str:
    """Type text into an input or textarea."""
    return await browser.type_text(selector, text)


@mcp.tool()
async def read_page() -> str:
    """Read the visible text from the current page."""
    return await browser.read()


@mcp.tool()
async def wait(seconds: float = 2) -> str:
    """Wait for the browser page to update."""
    return await browser.wait(seconds)


@mcp.tool()
async def screenshot() -> str:
    """Take a screenshot of the current browser page as visual evidence."""
    return await browser.screenshot()


if __name__ == "__main__":
    mcp.run()
