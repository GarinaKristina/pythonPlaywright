class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("//input[@id='gh-ac']")
        self.saved_button = page.locator(".saved")
        self.electronics_button = page.locator("//*[@class='hl-cat-nav__js-tab']//a[contains(text(),'Electronics')]")
        self.search_button = page.locator("#gh-btn")
        self.busket_icon = page.locator(".gh-cart-icon")


    def navigate(self):
       self.page.goto("https://www.ebay.com/")

    def fillFieldAndPressEnter(self, text):
       self.search_input.fill(text)
       self.search_input.press("Enter")
  

