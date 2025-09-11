
def test_check_status_code(page):
    page.goto("https://http.cat/")
    assert "HTTP Cats" in page.title()
    

def test_check_200_cat(page):
    page.goto("https://http.cat/")
    page.get_by_role("link", name=str("200")).click()
    page.wait_for_url("https://http.cat/status/200")
    assert "200" in page.title()

def test_check_404_cat(page):
    page.goto("https://http.cat/")
    page.get_by_role("link", name=str("404")).click()
    page.wait_for_url("https://http.cat/status/404")
    assert "404" in page.title()

def test_check_image_404(page):
    page.goto("https://http.cat/status/404")
    image = page.locator('img[src="/images/404.jpg"]')
    assert image.is_visible()
    assert "404" in image.get_attribute("src")

def test_invalidation_code_200_another_code(page):
    page.goto("https://http.cat/status/200")
    assert "200" in page.title()
    page.goto("https://http.cat/status/404")
    assert "404" in page.title()
    assert "200" not in page.title()