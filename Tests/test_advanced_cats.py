import pytest

@pytest.mark.parametrize(
    ["status_code", "url_validation"],
    [
        (404, "https://http.cat/status/404"),
        (401, "https://http.cat/status/401"),
        (200, "https://http.cat/status/200"),
        (500, "https://http.cat/status/500"),
    ],
    ids=["404", "401", "200", "500"]
)

def test_http_status(page, status_code, url_validation):
    page.goto('https://http.cat/')
    page.get_by_role("link", name=str(status_code)).click()
    page.wait_for_url(url_validation, timeout=10000)
    assert page.url == url_validation
    print(f"Tested URL: {page.url} for status code: {status_code}")
