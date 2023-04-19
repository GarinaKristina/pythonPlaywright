from pageObjects.MainPage import MainPage
from playwright.sync_api import Page, expect
import pytest

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

# import asyncio
# from playwright.async_api import async_playwright, expect

# async def main():
  
#     async with async_playwright() as p:
#       browser = await p.chromium.launch(headless=False)
#       page = await browser.new_page()
#       main_page = MainPage(page)

#       await main_page.navigate()
#       await expect (main_page.saved_button).to_have_text('Saved')
#       await expect (main_page.electronics_button).to_have_text('Electronics')
#       await main_page.fillFieldAndPressEnter("Smart")
#     # page.pause()
#     # page.screenshot(path="example.png")
#     # print(page.title())
#       await browser.close()

# asyncio.run(main())    