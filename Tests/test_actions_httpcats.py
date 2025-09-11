import pytest

@pytest.mark.parametrize(
    ["status_code", "url_validation"],
    [
        (404, "https://http.cat/status/404"),
        (401, "https://http.cat/status/401"),
    ],
    ids=["404", "401"]
)

def test_http_status_404(page, status_code, url_validation):
    page.goto('https://http.cat/')
    page.get_by_role("link", name=str(status_code)).click()
    page.wait_for_url(url_validation, timeout=10000) #Wait for navigation to complete

    if status_code == 404:
        assert page.url == url_validation
    else:
        assert page.url != "https://http.cat/status/404"
        print(f"Tested URL: {page.url} for status code: {status_code}")





'''def test_hover(page):
    page.goto('https://http.cat/')
    link = page.get_by_role("link", name="404 Not Found")
    link.hover()
    # Check if the title attribute is set correctly on hover
    assert link.get_attribute("title") == "404 Not Found"'''