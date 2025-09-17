import pytest

def test_initial_enter_on_page(page):
    page.goto("https://demoqa.com/")
    assert page.title() == "DEMOQA"
    page.wait_for_url("https://demoqa.com/") #Check if the tiltle of the page is correct
    assert page.url == "https://demoqa.com/" #Verify the URL is correct


def test_click_on_elements(page):
    page.goto("https://demoqa.com/")
    page.wait_for_url("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.wait_for_url("https://demoqa.com/elements")
    assert page.url == "https://demoqa.com/elements" #Verify the URL is correct after clicking on Elements    
    page.get_by_text("Check Box").click()
    page.wait_for_url("https://demoqa.com/checkbox")
    assert page.url == "https://demoqa.com/checkbox" #Verify the URL is correct after clicking on Check Box
    page.locator("label:has-text('Home')").click() # Check the "Home" checkbox by clicking on the visible label
    checkbox = page.locator("input[id='tree-node-home']")
    assert checkbox.is_checked()  # Verify if the checkbox is checked