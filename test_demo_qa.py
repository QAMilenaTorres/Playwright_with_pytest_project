import pytest

#def test_initial_enter_on_page(page):
   #page.goto("https://demoqa.com/")
   #assert page.title() == "DEMOQA"
   #page.wait_for_url("https://demoqa.com/") #Check if the tiltle of the page is correct
   #assert page.url == "https://demoqa.com/" #Verify the URL is correc

def test_checkbox(page):
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
    

    
    
def test_assert_title_and_type(page):
   page.goto("https://demoqa.com/")
   page.wait_for_url("https://demoqa.com/") #Check if the tiltle of the page is correct
   assert page.title() == "DEMOQA"
   assert page.url == "https://demoqa.com/" #Verify the URL is correct
   page.get_by_text("Elements").click()
   page.wait_for_url("https://demoqa.com/elements")
   assert page.url == "https://demoqa.com/elements" #Verify the URL is
   page.get_by_text("Text Box").click()
   page.wait_for_url("https://demoqa.com/text-box")
   assert page.url == "https://demoqa.com/text-box" #Verify the URL is correct after clicking on Text Box
   page.get_by_placeholder("Full Name").click()
   page.get_by_placeholder("Full Name").fill("Senhor Patinhas")
   if page.get_by_placeholder("Full Name").input_value() == "Senhor Patinhas":
       print("O valor foi inserido corretamente.")
   else:
       raise AssertionError("O valor não foi inserido corretamente.")

#def test_