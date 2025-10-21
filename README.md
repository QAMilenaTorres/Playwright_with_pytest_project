# 🐍 Python Playwright Tests

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4.1-brightgreen)](https://docs.pytest.org/en/8.4.x/)
[![Playwright](https://img.shields.io/badge/Playwright-Python-orange)](https://playwright.dev/python/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Este repositório contém **testes automatizados usando Playwright + Pytest** para validação de sites.  
Ele demonstra **automação de frontend**, **validação de elementos**, **interação com formulários**, e geração de **relatórios HTML**. Também pode ser integrado com **pipelines de CI/CD**.

---

## 🛠 Tecnologias Utilizadas

- 🐍 **Python 3.10+**  
- 🎭 **Playwright** (Python) – automação de navegador  
- ⚡ **Pytest** – framework de testes  
- 📄 **Pytest-HTML** – geração de relatórios em HTML  

---

## 📂 Estrutura do Projeto

```text
python-playwright-tests/
│
├─ Tests/                  # Testes automatizados
│  ├─ test_demo_qa.py
│  └─ conftest.py
│
├─ screenshots/            # Prints de testes
├─ requirements.txt        # Dependências do Python
└─ README.md               # Documentação

## 🚀 Como Rodar os Testes Localmente

# Clone o repositório
git clone https://github.com/QAMilenaTorres/python-playwright-tests.git
cd python-playwright-tests

# Instale dependências
pip install -r requirements.txt

# Instale navegadores do Playwright
playwright install

# Execute os testes
pytest --html=report.html --self-contained-html
**⚠️ Dica: Use a flag --html=report.html para gerar relatórios detalhados em HTML de cada execução de teste.**

🧪 Recursos Incluídos

# Testes de navegação em páginas web

# Validação de títulos, elementos e formulários

# Captura de screenshots automáticas em falhas

# Relatórios HTML detalhados para análise de resultados