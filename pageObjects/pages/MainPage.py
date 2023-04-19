from pageObjects.locators.MainPageLocators import MainPageLocators
class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator(MainPageLocators.search_input)
        self.saved_button = page.locator(MainPageLocators.saved_button)
        self.electronics_button = page.locator(MainPageLocators.electronics_button)
        self.search_button = page.locator(MainPageLocators.search_button)
        self.busket_icon = page.locator(MainPageLocators.busket_icon)


    def navigate(self):
       self.page.goto("https://www.ebay.com/")

    def fillFieldAndPressEnter(self, text):
       self.search_input.fill(text)
       self.search_input.press("Enter")
  

