import pytest

# Hook do pytest-html para anexar prints no relatório
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

# Se o teste falhar ou for marcado como xfail mas falhar de verdade
if report.when == "call":
    page = item.funcargs.get("page", None)  # pega a fixture page do Playwright
    if page:
        screenshot_path = f"screenshots/{item.name}.png"
        page.screenshot(path=screenshot_path)
        # Adiciona screenshot no relatório HTML
        pytest_html = item.config.pluginmanager.getplugin("html")
        extra.append(pytest_html.extras.png(screenshot_path))
report.extra = extra