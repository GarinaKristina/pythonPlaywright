class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("//input[@id='gh-ac']")
        self.saved_button = page.locator(".saved")
        self.electronics_button = page.locator("//li[@class='hl-cat-nav__js-tab']//a[contains(text(),'Electronics')]")

    async def navigate(self):
       await self.page.goto("https://www.ebay.com/")

    async def fillFieldAndPressEnter(self, text):
       await self.search_input.fill(text)
       await self.search_input.press("Enter")
  

