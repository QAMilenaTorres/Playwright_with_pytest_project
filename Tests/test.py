from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example Domain" in page.title()
        browser.close()


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")  # roda sem abrir janela
    options.add_argument("--disable-gpu")
    service = Service()  # usa o chromedriver do PATH
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_google_title(driver):
    """Verifica se o título do Google é correto"""
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_search_box_present(driver):
    """Verifica se a barra de pesquisa do Google está presente"""
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed()
