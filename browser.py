from pathlib import Path

from playwright.async_api import async_playwright


SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)


class Browser:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def start(self):
        if self.page:
            return

        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=True
        )

        context = await self.browser.new_context(
            viewport={"width": 1280, "height": 720},
            device_scale_factor=1,
        )

        self.page = await context.new_page()

    async def open(self, url: str) -> str:
        await self.start()

        await self.page.goto(
            url,
            wait_until="domcontentloaded",
        )

        return f"Opened {self.page.url}"

    async def click(self, selector: str) -> str:
        await self.start()

        await self.page.locator(selector).click()

        return f"Clicked: {selector}"

    async def type_text(self, selector: str, text: str) -> str:
        await self.start()

        await self.page.locator(selector).fill(text)

        return f"Typed into: {selector}"

    async def read(self) -> str:
        await self.start()

        return await self.page.locator("body").inner_text()

    async def wait(self, seconds: float = 2) -> str:
        await self.start()

        await self.page.wait_for_timeout(seconds * 1000)

        return f"Waited {seconds} seconds"

    async def screenshot(self) -> str:
        await self.start()

        path = SCREENSHOT_DIR / "latest.png"

        await self.page.screenshot(
            path=str(path),
            full_page=True,
        )

        return f"Screenshot saved to {path}"


browser = Browser()
