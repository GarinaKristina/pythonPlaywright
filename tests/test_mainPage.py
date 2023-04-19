from pageObjects.MainPage import MainPage
import re
from playwright.sync_api import Page, expect

def test_main_page_has_buttons_with_text(page: Page):
    main_page = MainPage(page)
    main_page.navigate()
    expect (main_page.saved_button).to_have_text('Saved')
    expect (main_page.electronics_button).to_have_text('Electronics')

def test_main_page_has_visible_elements(page: Page):   
    main_page = MainPage(page)
    main_page.navigate() 
    expect (main_page.search_button).to_be_visible()
    expect (main_page.busket_icon).to_be_visible()


def test_main_page_search_input(page: Page): 
    main_page = MainPage(page)
    main_page.navigate()  
    main_page.fillFieldAndPressEnter("Smart")
    expect(page).to_have_title(re.compile("Smart for sale | eBay"))
