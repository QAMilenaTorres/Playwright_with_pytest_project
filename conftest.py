import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Executa o hook e pega o resultado
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Aqui você pode acessar o contexto do teste
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Screenshot salvo em: {screenshot_path}")
    