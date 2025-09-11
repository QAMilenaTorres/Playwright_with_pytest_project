# 🐍 Playwright + Pytest Project

Este repositório contém **testes automatizados** usando [Playwright](https://playwright.dev/python/) + [Pytest](https://docs.pytest.org/) para validação de sites.  
Os testes cobrem desde casos simples até cenários avançados com parametrização.

---

## 🛠 Tecnologias utilizadas

- 🐍 **Python 3.10+**
- 🎭 **Playwright (Python)**
- ⚡ **Pytest**
- 📄 **Pytest-HTML** (para relatórios)
- 📸 **Screenshots automáticos** em falhas

---

## 🚀 Como rodar os testes localmente

1️⃣ Clone o repositório:
```bash
git clone https://github.com/QAMilenaTorres/python-playwright-tests.git
cd python-playwright-tests

📂 Estrutura do projeto
Playwright_with_pytest_project/
│── tests/
│   ├── test_basic_cats.py       # Testes simples de status code
│   ├── test_advanced_cats.py    # Testes avançados com parametrização
│   ├── test_actions_httpcats.py # Testes de cliques e validações
│   ├── test_google.py           # Teste de abertura do Google
│   └── test.py                  # Teste inicial
│── conftest.py                  # Configuração global do pytest
│── requirements.txt             # Dependências do projeto
│── README.md                    # Documentação do projeto


