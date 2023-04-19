from playwright.sync_api import Locator

class MainPageLocators:
    search_input: Locator = "//input[@id='gh-ac']"
    saved_button: Locator = ".saved"
    electronics_button: Locator = "//*[@class='hl-cat-nav__js-tab']//a[contains(text(),'Electronics')]"
    search_button: Locator = "#gh-btn"
    busket_icon: Locator = ".gh-cart-icon"
