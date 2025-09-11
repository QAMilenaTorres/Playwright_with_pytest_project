def test_abrir_google(page):
    page.goto("https://www.google.com/")
    print("Título da página:", page.title())
    assert "Google" in page.title()

